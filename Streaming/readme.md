In addition to doing everything manually and using cloudera manager, we also
tried using StreamSets which was much easier and quicker to use. Notes for
StreamSets are [here](streamsets.md)

# The Flume config:
Once we were able to write directly to an hbase sink, we commented out
and enabled the kafka sink. No other configuration for kafka was needed, 
other then increasing the record memory and enabling auto topic
creation.

```
#Sources, channels, and sinks are defined per
# agent name, in this case 'tier1'.
tier1.sources  = source1
tier1.channels = channel1
tier1.sinks    = sink1

# For each source, channel, and sink, set
# standard properties.
tier1.sources.source1.type     = netcat
#tier1.sources.source1.bind     = 127.0.0.1
tier1.sources.source1.bind = ip-172-31-43-253.us-west-2.compute.internal
tier1.sources.source1.port     = 9999
tier1.sources.source1.channels = channel1
tier1.channels.channel1.type   = memory

# Hbase Sink
tier1.sinks.sink1.type = hbase
tier1.sinks.sink1.channel     = channel1
tier1.sinks.sink1.table = measurements
tier1.sinks.sink1.columnFamily = cf
tier1.sinks.sink1.batchSize = 100
tier1.sinks.sink1.serializer = org.apache.flume.sink.hbase.SimpleHbaseEventSerializer

# Kafka Sink
tier1.sinks.sink1.type = org.apache.flume.sink.kafka.KafkaSink
tier1.sinks.sink1.topic = measurements
tier1.sinks.sink1.brokerList = ip-172-31-43-253.us-west-2.compute.internal:9092
tier1.sinks.sink1.channel = channel1
tier1.sinks.sink1.batchSize = 100
```

# use tool to generate data
```
java -cp bootcamp-0.0.1-SNAPSHOT.jar com.cloudera.fce.bootcamp.MeasurementGenerator ip-172-31-43-253.us-west-2.compute.internal 9999
```

# check kafka topics
```
kafka-topics  --zookeeper  ip-172-31-47-126.us-west-2.compute.internal:2181 --list
```

# consume from kafka topic
```
kafka-console-consumer --zookeeper ip-172-31-47-126.us-west-2.compute.internal:2181 --topic measurements
```

# Run spark streaming script
```
SPARK_EX_JAR=/opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/spark/lib/spark-examples.jar
spark-submit --master yarn --conf "spark.dynamicAllocation.enabled=false" --driver-memory 4g --executor-memory 2g --jars $SPARK_EX_JAR spark_streaming.py
```

# Spark streaming
Note, we attempted to do spark streaming in scala and python. The scripts are in the `Streaming`
directory. For scala, we were able to write to hdfs and hbase. For python, we were able
to write to hdfs and to kudu. Pyspark errors are not always helpful, often times it prints
the error location as the location in the java library code.

# To install kudu-python:
In order to install the kudu python client for use in spark, some amount of work was needed:
```
[ec2-user@ip-172-31-43-253 ~]$ sudo yum install wget
[ec2-user@ip-172-31-43-253 ~]$ wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
[ec2-user@ip-172-31-43-253 ~]$ sudo rpm -ivh epel-release-7-9.noarch.rpm
[ec2-user@ip-172-31-43-253 ~]$ sudo yum clean all
[ec2-user@ip-172-31-43-253 ~]$ sudo yum install epel-release
[ec2-user@ip-172-31-43-253 ~]$ sudo yum install python-pip
[root@ip-172-31-43-253 ec2-user]# pip install kudu-python -v
[root@ip-172-31-43-253 ec2-user]# pip install kudu-python -v --no-cache-dir
[root@ip-172-31-43-253 ec2-user]# vim /tmp/pip-b^C
[root@ip-172-31-43-253 ec2-user]# cd /usr/include
[root@ip-172-31-43-253 include]# ln -s /opt/cloudera/parcels/KUDU-1.3.0-1.cdh5.11.1.p0.27/include/kudu kudu
[root@ip-172-31-43-253 include]# yum install gcc
[root@ip-172-31-43-253 include]# yum install  gcc-c++
[root@ip-172-31-43-253 include]# yum install python-devel
[root@ip-172-31-43-253 lib64]# cp /opt/cloudera/parcels/KUDU-1.3.0-1.cdh5.11.1.p0.27/lib64/libkudu_client.so* ./
[root@ip-172-31-43-253 lib64]# pip install kudu-python -v --no-cache-dir
```

