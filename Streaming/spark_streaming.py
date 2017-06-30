#!/usr/bin/python2.7

from __future__ import print_function

import sys
import time

import kudu
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

HDFS_PATH = 'hdfs://ip-172-31-47-126.us-west-2.compute.internal:8020/tmp'
ZKQUOROM = 'ip-172-31-47-126.us-west-2.compute.internal:2181'
TOPIC = 'measurements'
KUDU_MASTER = 'ip-172-31-32-134.us-west-2.compute.internal'

TO_KUDU = True
TO_HDFS = False


def get_path():
  # for hdfs saving, we want to generate a unique file path each time so they don't
  # collide. The downside of this is that we generate a ton of files
  return "%s/%s" % (HDFS_PATH, str(int(time.time() * 1000)))

def insert_to_kudu(rdd):
  client = kudu.connect(host=KUDU_MASTER, port=7051)
  table = client.table('galaxy_measurements')
  session = client.new_session()

  for line in rdd.toLocalIterator():
    cols = line.split(',')
    op = table.new_insert({
      'measurement_id': cols[0],
      'detector_id': int(cols[1]),
      'galaxy_id': int(cols[2]),
      'astrophysicist_id': int(cols[3]),
      'measurement_time': float(cols[4]),
      'amplitude_1': float(cols[5]),
      'amplitude_2': float(cols[6]),
      'amplitude_3': float(cols[7]),
      'wave': float(cols[5]) > 0.995 and float(cols[7]) > 0.995 and float(cols[6]) < 0.005,
    })

    session.apply(op)
    session.flush()

def main():
  sc = SparkContext(appName="PythonStreamingKafka")
  ssc = StreamingContext(sc, 10)

  kvs = KafkaUtils.createStream(ssc, ZKQUOROM, "spark-streaming-consumer", {TOPIC: 1})
  lines = kvs.map(lambda x: x[1])

  if TO_KUDU:
    lines.foreachRDD(insert_to_kudu)
    lines.pprint()


  if TO_HDFS:
    lines.foreachRDD(lambda rdd: rdd.saveAsTextFile(get_path()) if rdd.count() != 0 else None)

  ssc.start()
  ssc.awaitTermination()

if __name__ == "__main__":
  main()

