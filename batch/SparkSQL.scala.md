### Spark Code
```
import org.apache.spark._
import org.apache.spark.SparkContext._

val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

sqlContext.sql("Drop table tbl_spark_gravitational ")

sqlContext.sql("Create table if not exists tbl_spark_gravitational as select a.detector_id,a.galaxy_id,a.amplitude_1,a.amplitude_2,a.amplitude_3, IF(a.amplitude_1 > 0.995 and a.amplitude_3>0.995 and a.amplitude_2 <0.005, 'Yes', 'No') as gravitational_wave from measurements a, detectors b, galaxies c where a.detector_id=b.detector_id and a.galaxy_id=c.galaxy_id")

exit
```


