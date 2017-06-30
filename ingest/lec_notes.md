* ELT vs ETL
* it can often make sense to keep the raw around after transformation

* ingesting files:
  * easy, make the file visible to the edge node and then do a hdfs put
  * make the files visible via local disk or NAS
  * oozie is not to be a great idea for scheduling these types of jobs, they
    should just pay money for a specialized tool (that they probably already
    have)

* sqoop is just a CLI tool. no install required, no long running process
  * runs a mapper only job to oepn a jdbc conn and pull down data
  * be careful on how hard you hammer the rdbms
  * sqoop can also export to rdbms but that's not normal
* additionally, spark sql jdbc has been starting to gain traction
  * this has the advantage that the data does not have to hit hdfs,
    BUT that does mean you do not get to keep the raw data

* Querying
  * the datamodel that people query is not necessarily the data model as
    what was ingested. That is what the TRANSFORM is.

  * impala is not meant for ETL, huge transforms etc.
    * it is meant for end user data access
    * it may not be as flexible as hive, but it is much easier to use

* key lookups: hbase and kudu

* see columnar file formats. so if you only want a subset of columns you don't have to
  pull all columns then filter out the ones you don't want
  * see: avro vs. parquet
  * generally want to use parquet for impala

* the hive metastore can store statistics information about my impala queries
  * use 'compute stats' command

* don't let your partitioning get TOO crazy. too many partitions is also slow
* structure your data too improve performance.

# work
* use sqoop to read from rdbms
* more import parallelism
* write directly to parquet
* compression@
* ingest straight into a table
* convert double to decimals (which is not ieee, but avoids rounding errors)

# partitioning
If you have too many partitions, they can run out of memory writing the partitions.
A solution too that is to sort the data by partition key first... but then you have
to pay the sort cost first.

