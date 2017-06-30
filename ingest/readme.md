# create tables in hive

This is a naive creation, no partitioning or external tables. We later switched
amplitude columns to be type decimal(32,32). With decimal(24,18), some rows
had amplitudes with values of 'null'. This resulted in us not detecting
nine of the gravitational wave. We initially detected onlyl 47 of the 56 waves.

```
create table measurements (
  measurement_id string,
  detector_id bigint,
  galaxy_id bigint,
  astrophysicist_id bigint,
  measurement_time bigint,
  amplitude_1 decimal(24,18),
  amplitude_2 decimal(24,18),
  amplitude_3 decimal(24,18)
);

create table detectors (
  detector_id int,
  detector_name string,
  country string,
  latitude decimal(12,5),
  longitude decimal(12,5)
);

create table galaxies (
  galaxy_id int,
  galaxy_name string,
  galaxy_type string,
  distance_ly decimal(12,3),
  absolute_magnitude decimal(12,3),
  apparent_magnitude decimal(12,3),
  galaxy_group string
);

create table astrophysicists (
  astrophysicist_id int,
  astrophysicist_name string,
  year_of_birth int,
  nationality string
);
```

# Oracle JDBC
* place in `/var/lib/sqoop` for all machines

# Import commands
```
sqoop import --connect jdbc:oracle:thin:@gravity.cghfmcr8k3ia.us-west-2.rds.amazonaws.com:15210:gravity --table MEASUREMENTS --username gravity --password bootcamp -m 1

sqoop import --connect jdbc:oracle:thin:@gravity.cghfmcr8k3ia.us-west-2.rds.amazonaws.com:15210:gravity --table GALAXIES --username gravity --password bootcamp --hive-import --hive-table galaxies -m 1

sqoop import --connect jdbc:oracle:thin:@gravity.cghfmcr8k3ia.us-west-2.rds.amazonaws.com:15210:gravity --table DETECTORS --username gravity --password bootcamp --hive-import --hive-table detectors -m 1

sqoop import --connect jdbc:oracle:thin:@gravity.cghfmcr8k3ia.us-west-2.rds.amazonaws.com:15210:gravity --table ASTROPHYSICISTS --username gravity --password bootcamp --hive-import --hive-table astrophysicists -m 1
```
* additionally, use `--direct` for better performance. Not safe if source db is being written to at the same time
* `-m` changes the number of map jobs. `-m 8` will produce significantly better performance
* do not use `split-by` with `direct` (`--split-by measurement_id`)
* the following is faster:

```
sqoop import --connect jdbc:oracle:thin:@gravity.cghfmcr8k3ia.us-west-2.rds.amazonaws.com:15210:gravity --table MEASUREMENTS --username gravity --password bootcamp --hive-import --hive-table measurements -m 8 —-direct
```

# Create View to find gravitational waves
```
create view vw_gravitational_wave
as
select a.detector_id,from_unixtime(CAST(a.measurement_time/1000 as BIGINT), 'yyyy/MM/dd HH:mm') as measurement_time,a.galaxy_id,a.amplitude_1,a.amplitude_2,a.amplitude_3 from measurements a, detectors b, galaxies c
where a.detector_id=b.detector_id and a.galaxy_id=c.galaxy_id and
a.amplitude_1 > 0.995 and a.amplitude_3>0.995 and a.amplitude_2 <0.005
```

# Copy measurements to parquet
```
set COMPRESSION_CODEC=snappy;

CREATE EXTERNAL TABLE measurements_parquet
  STORED AS parquet
  LOCATION '/user/hdfs/OracleTables/parquet'
AS
  SELECT * FROM measurements;
```

then from this new parquet compressed table, create a new view on top of it!
