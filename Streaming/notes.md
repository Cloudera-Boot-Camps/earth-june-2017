# Stream Processing

* ingesting and transforming as the events happen
* a persistent process
* usually from a queue

* some stream processing is real time and others are sort of micro
  batch processing.
  * it really comes down to latency
  * micro batch processing is still batching over low latency so
    it's still mostly real time while possibly improving performance
  * quite often it doesn't really matter whether it's millisecond
    or a few second granularity

# Flume
* stream ingestion component
* bringing data into the cluster and not so much transformation
* architecture:
  * agents that run on the cluster and listen for new records
  * **upsteam** data source sends data
  * records comes from **source**
  * buffered into a **channel**
  * sent out to a **sink**
  * interceptors can be written to insert lightweight custom code transforms
    * this doesn't allow exploding or merging multiple records together
* ACKs can be sent out by the channel to the upstream

  * in flume, memory channels are going to give you the best
    throughput but you lose durability in crashes
  * kafka can be used as a channel (!)

* kafka is a pub-sub system
  * a scalable queue of records
  * records are not removed from the topic when they are consumed
    * therefore each consumer needs to keep track of it's topic offset

  * you can only append records (no deletion, modification)
  * kafka will not ack to producer that record was received until a
    certain number of brokers have written that record to disk

* you can use flume to ingest and have kafka as your channel and no sink!
  * it's weird and against the normal spirit of things but it works

# Spark Streaming
  * for transforming and processing the data
  * process arriving records in micro batches in seconds granularity
  * spark streaing envelope - pre-made spark ETL application
