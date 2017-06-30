### Spark Script
```
import org.apache.spark.SparkConf
import org.apache.spark.streaming._
import org.apache.spark.streaming.kafka._
import org.apache.hadoop.hbase._
import org.apache.hadoop.hbase.TableName
import org.apache.hadoop.hbase.client._
import org.apache.hadoop.hbase.util.Bytes


val zkQuorum="ip-172-31-47-126.us-west-2.compute.internal:2181"
val group="spark-streaming-kafka"
val topic="mesurements"
val con = ConnectionFactory.createConnection()
val table = con.getTable(TableName.valueOf("measurements")) 
print(table)

//#val sparkConf = new SparkConf().setAppName("KafkaSparkStreaming")
val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint("checkpoint")

val kafkaStream = KafkaUtils.createStream(ssc,zkQuorum,group,Map(("measurements",1))).map(_._2)

kafkaStream.print()

kafkaStream.foreachRDD((rdd,time) => {
 //rdd.print()
  rdd.foreach(line => {
          val con = ConnectionFactory.createConnection()
          try {
            val table = con.getTable(TableName.valueOf("measurements"))
            val cells = line.split(",")
            val put = new Put(Bytes.toBytes(cells(0)))
            val cf = Bytes.toBytes("cf")
            put.addColumn(cf, Bytes.toBytes("detector_id"), Bytes.toBytes(cells(1)))
            put.addColumn(cf, Bytes.toBytes("galaxy_id"), Bytes.toBytes(cells(2)))
            put.addColumn(cf, Bytes.toBytes("astrophysicist_id"), Bytes.toBytes(cells(3)))
            put.addColumn(cf, Bytes.toBytes("measurement_time"), Bytes.toBytes(cells(4)))
            put.addColumn(cf, Bytes.toBytes("amplitude_1"), Bytes.toBytes(cells(5)))
            put.addColumn(cf, Bytes.toBytes("amplitude_2"), Bytes.toBytes(cells(6)))
            put.addColumn(cf, Bytes.toBytes("amplitude_3"), Bytes.toBytes(cells(7)))
            table.put(put)

	      } catch {
                case e: Exception =>println(e)
		
		}
		finally {
		 con.close()
		}

	})

})


//kafkaStream.take(10).foreach(println)
ssc.start()
ssc.awaitTermination()
```

