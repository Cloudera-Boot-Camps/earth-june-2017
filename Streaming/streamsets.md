Step one: install jdk 1.8:

```
wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
```


Step 2: install streamsets:

```
[ec2-user@ip-172-31-32-134 streamsets-datacollector-2.6.0.1-all-rpms]$ sudo yum localinstall streamsets*.rpm
Loaded plugins: amazon-id, rhui-lb, search-disabled-repos
Examining streamsets-datacollector-2.6.0.1-1.noarch.rpm: streamsets-datacollector-2.6.0.1-1.noarch
Marking streamsets-datacollector-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-aws-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-aws-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-aws-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-azure-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-azure-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-azure-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-basic-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-basic-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-basic-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-jms-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-jms-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-jms-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-redis-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-redis-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-redis-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch.rpm to be installed
Examining streamsets-datacollector-stats-lib-2.6.0.1-1.noarch.rpm: streamsets-datacollector-stats-lib-2.6.0.1-1.noarch
Marking streamsets-datacollector-stats-lib-2.6.0.1-1.noarch.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package streamsets-datacollector.noarch 0:2.6.0.1-1 will be installed
--> Processing Dependency: jre >= 1.8 for package: streamsets-datacollector-2.6.0.1-1.noarch
cloudera-manager                                                                      |  951 B  00:00:00
rhui-REGION-client-config-server-7                                                    | 2.9 kB  00:00:00
rhui-REGION-rhel-server-releases                                                      | 3.5 kB  00:00:00
rhui-REGION-rhel-server-rh-common                                                     | 3.8 kB  00:00:00
(1/2): rhui-REGION-rhel-server-releases/7Server/x86_64/updateinfo                     | 1.9 MB  00:00:00
(2/2): rhui-REGION-rhel-server-releases/7Server/x86_64/primary_db                     |  38 MB  00:00:00
---> Package streamsets-datacollector-apache-kafka_0_10-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kafka_0_8_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kafka_0_8_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kafka_0_9-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kudu_1_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kudu_1_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kudu_1_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-kudu_1_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-apache-solr_6_1_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-aws-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-azure-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-basic-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-bigtable-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cassandra_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_10-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_11-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_4-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_5-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_7-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_8-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_5_9-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_kafka_1_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-cdh_spark_2_1_r1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-elasticsearch_5-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-groovy_2_4-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-hdp_2_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-hdp_2_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-hdp_2_4-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-hdp_2_5-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-hdp_2_6-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-influxdb_0_9-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-jdbc-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-jms-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-jython_2_7-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mapr_5_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mapr_5_1-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mapr_5_2-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mongodb_3-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-mysql-binlog-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-omniture-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-rabbitmq-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-redis-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-salesforce-lib.noarch 0:2.6.0.1-1 will be installed
---> Package streamsets-datacollector-stats-lib.noarch 0:2.6.0.1-1 will be installed
--> Running transaction check
---> Package java-1.8.0-openjdk.x86_64 1:1.8.0.131-3.b12.el7_3 will be installed
--> Processing Dependency: java-1.8.0-openjdk-headless = 1:1.8.0.131-3.b12.el7_3 for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: fontconfig(x86-64) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libasound.so.2(ALSA_0.9)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libasound.so.2(ALSA_0.9.0rc4)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjava.so(SUNWprivate_1.1)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjli.so(SUNWprivate_1.1)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjpeg.so.62(LIBJPEG_6.2)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjvm.so(SUNWprivate_1.1)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libpng15.so.15(PNG15_0)(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: xorg-x11-fonts-Type1 for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libX11.so.6()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libXcomposite.so.1()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libXext.so.6()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libXi.so.6()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libXrender.so.1()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libXtst.so.6()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libasound.so.2()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libawt.so()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libgif.so.4()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjava.so()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjli.so()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjpeg.so.62()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libjvm.so()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: libpng15.so.15()(64bit) for package: 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64
--> Running transaction check
---> Package alsa-lib.x86_64 0:1.1.1-1.el7 will be installed
---> Package fontconfig.x86_64 0:2.10.95-10.el7 will be installed
--> Processing Dependency: fontpackages-filesystem for package: fontconfig-2.10.95-10.el7.x86_64
---> Package giflib.x86_64 0:4.1.6-9.el7 will be installed
--> Processing Dependency: libICE.so.6()(64bit) for package: giflib-4.1.6-9.el7.x86_64
--> Processing Dependency: libSM.so.6()(64bit) for package: giflib-4.1.6-9.el7.x86_64
---> Package java-1.8.0-openjdk-headless.x86_64 1:1.8.0.131-3.b12.el7_3 will be installed
--> Processing Dependency: chkconfig >= 1.7 for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: chkconfig >= 1.7 for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: copy-jdk-configs >= 1.1-3 for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: nss(x86-64) >= 3.28.4 for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: tzdata-java >= 2015d for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: jpackage-utils for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
--> Processing Dependency: lksctp-tools(x86-64) for package: 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64
---> Package libX11.x86_64 0:1.6.3-3.el7 will be installed
--> Processing Dependency: libX11-common >= 1.6.3-3.el7 for package: libX11-1.6.3-3.el7.x86_64
--> Processing Dependency: libxcb.so.1()(64bit) for package: libX11-1.6.3-3.el7.x86_64
---> Package libXcomposite.x86_64 0:0.4.4-4.1.el7 will be installed
---> Package libXext.x86_64 0:1.3.3-3.el7 will be installed
---> Package libXi.x86_64 0:1.7.4-2.el7 will be installed
---> Package libXrender.x86_64 0:0.9.8-2.1.el7 will be installed
---> Package libXtst.x86_64 0:1.2.2-2.1.el7 will be installed
---> Package libjpeg-turbo.x86_64 0:1.2.90-5.el7 will be installed
---> Package libpng.x86_64 2:1.5.13-7.el7_2 will be installed
---> Package xorg-x11-fonts-Type1.noarch 0:7.5-9.el7 will be installed
--> Processing Dependency: mkfontdir for package: xorg-x11-fonts-Type1-7.5-9.el7.noarch
--> Processing Dependency: mkfontdir for package: xorg-x11-fonts-Type1-7.5-9.el7.noarch
--> Processing Dependency: ttmkfdir for package: xorg-x11-fonts-Type1-7.5-9.el7.noarch
--> Processing Dependency: ttmkfdir for package: xorg-x11-fonts-Type1-7.5-9.el7.noarch
--> Running transaction check
---> Package chkconfig.x86_64 0:1.3.61-5.el7_2.1 will be updated
---> Package chkconfig.x86_64 0:1.7.2-1.el7_3.1 will be an update
---> Package copy-jdk-configs.noarch 0:1.2-1.el7 will be installed
---> Package fontpackages-filesystem.noarch 0:1.44-8.el7 will be installed
---> Package javapackages-tools.noarch 0:3.4.1-11.el7 will be installed
--> Processing Dependency: python-javapackages = 3.4.1-11.el7 for package: javapackages-tools-3.4.1-11.el7.noarch
---> Package libICE.x86_64 0:1.0.9-2.el7 will be installed
---> Package libSM.x86_64 0:1.2.2-2.el7 will be installed
---> Package libX11-common.noarch 0:1.6.3-3.el7 will be installed
---> Package libxcb.x86_64 0:1.11-4.el7 will be installed
--> Processing Dependency: libXau.so.6()(64bit) for package: libxcb-1.11-4.el7.x86_64
---> Package lksctp-tools.x86_64 0:1.0.17-2.el7 will be installed
---> Package nss.x86_64 0:3.21.0-9.el7_2 will be updated
--> Processing Dependency: nss = 3.21.0-9.el7_2 for package: nss-sysinit-3.21.0-9.el7_2.x86_64
--> Processing Dependency: nss(x86-64) = 3.21.0-9.el7_2 for package: nss-tools-3.21.0-9.el7_2.x86_64
---> Package nss.x86_64 0:3.28.4-1.2.el7_3 will be an update
--> Processing Dependency: nspr >= 4.13.1 for package: nss-3.28.4-1.2.el7_3.x86_64
--> Processing Dependency: nss-util >= 3.28.2-1.1 for package: nss-3.28.4-1.2.el7_3.x86_64
--> Processing Dependency: libnssutil3.so(NSSUTIL_3.24)(64bit) for package: nss-3.28.4-1.2.el7_3.x86_64
---> Package ttmkfdir.x86_64 0:3.0.9-42.el7 will be installed
---> Package tzdata-java.noarch 0:2017b-1.el7 will be installed
---> Package xorg-x11-font-utils.x86_64 1:7.5-20.el7 will be installed
--> Processing Dependency: libXfont.so.1()(64bit) for package: 1:xorg-x11-font-utils-7.5-20.el7.x86_64
--> Processing Dependency: libfontenc.so.1()(64bit) for package: 1:xorg-x11-font-utils-7.5-20.el7.x86_64
--> Running transaction check
---> Package libXau.x86_64 0:1.0.8-2.1.el7 will be installed
---> Package libXfont.x86_64 0:1.5.1-2.el7 will be installed
---> Package libfontenc.x86_64 0:1.1.2-3.el7 will be installed
---> Package nspr.x86_64 0:4.11.0-1.el7_2 will be updated
---> Package nspr.x86_64 0:4.13.1-1.0.el7_3 will be an update
---> Package nss-sysinit.x86_64 0:3.21.0-9.el7_2 will be updated
---> Package nss-sysinit.x86_64 0:3.28.4-1.2.el7_3 will be an update
---> Package nss-tools.x86_64 0:3.21.0-9.el7_2 will be updated
---> Package nss-tools.x86_64 0:3.28.4-1.2.el7_3 will be an update
---> Package nss-util.x86_64 0:3.21.0-2.2.el7_2 will be updated
---> Package nss-util.x86_64 0:3.28.4-1.0.el7_3 will be an update
---> Package python-javapackages.noarch 0:3.4.1-11.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=============================================================================================================
 Package                                      Arch   Version          Repository                        Size
=============================================================================================================
Installing:
 streamsets-datacollector                     noarch 2.6.0.1-1        /streamsets-datacollector-2.6.0.1-1.noarch
                                                                                                       161 M
 streamsets-datacollector-apache-kafka_0_10-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch
                                                                                                        36 M
 streamsets-datacollector-apache-kafka_0_8_1-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch
                                                                                                        37 M
 streamsets-datacollector-apache-kafka_0_8_2-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch
                                                                                                        34 M
 streamsets-datacollector-apache-kafka_0_9-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch
                                                                                                        36 M
 streamsets-datacollector-apache-kudu_1_0-lib noarch 2.6.0.1-1        /streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch
                                                                                                        19 M
 streamsets-datacollector-apache-kudu_1_1-lib noarch 2.6.0.1-1        /streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch
                                                                                                        19 M
 streamsets-datacollector-apache-kudu_1_2-lib noarch 2.6.0.1-1        /streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch
                                                                                                        19 M
 streamsets-datacollector-apache-kudu_1_3-lib noarch 2.6.0.1-1        /streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch
                                                                                                        19 M
 streamsets-datacollector-apache-solr_6_1_0-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch
                                                                                                        15 M
 streamsets-datacollector-aws-lib             noarch 2.6.0.1-1        /streamsets-datacollector-aws-lib-2.6.0.1-1.noarch
                                                                                                        41 M
 streamsets-datacollector-azure-lib           noarch 2.6.0.1-1        /streamsets-datacollector-azure-lib-2.6.0.1-1.noarch
                                                                                                        13 M
 streamsets-datacollector-basic-lib           noarch 2.6.0.1-1        /streamsets-datacollector-basic-lib-2.6.0.1-1.noarch
                                                                                                        32 M
 streamsets-datacollector-bigtable-lib        noarch 2.6.0.1-1        /streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch
                                                                                                        47 M
 streamsets-datacollector-cassandra_3-lib     noarch 2.6.0.1-1        /streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch
                                                                                                        15 M
 streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
                                                                                                        28 M
 streamsets-datacollector-cdh_5_10-lib        noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch
                                                                                                       201 M
 streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
                                                                                                        28 M
 streamsets-datacollector-cdh_5_11-lib        noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch
                                                                                                       204 M
 streamsets-datacollector-cdh_5_2-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch
                                                                                                        65 M
 streamsets-datacollector-cdh_5_3-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch
                                                                                                        87 M
 streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch
                                                                                                        27 M
 streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
                                                                                                        27 M
 streamsets-datacollector-cdh_5_4-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch
                                                                                                       202 M
 streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
                                                                                                        27 M
 streamsets-datacollector-cdh_5_5-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch
                                                                                                       188 M
 streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
                                                                                                        28 M
 streamsets-datacollector-cdh_5_7-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch
                                                                                                       197 M
 streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
                                                                                                        28 M
 streamsets-datacollector-cdh_5_8-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch
                                                                                                       200 M
 streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
                                                                                                        28 M
 streamsets-datacollector-cdh_5_9-lib         noarch 2.6.0.1-1        /streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch
                                                                                                       200 M
 streamsets-datacollector-cdh_kafka_1_2-lib   noarch 2.6.0.1-1        /streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch
                                                                                                        40 M
 streamsets-datacollector-cdh_kafka_1_3-lib   noarch 2.6.0.1-1        /streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch
                                                                                                        40 M
 streamsets-datacollector-cdh_kafka_2_0-lib   noarch 2.6.0.1-1        /streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch
                                                                                                        41 M
 streamsets-datacollector-cdh_kafka_2_1-lib   noarch 2.6.0.1-1        /streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch
                                                                                                        41 M
 streamsets-datacollector-cdh_spark_2_1_r1-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch
                                                                                                       103 M
 streamsets-datacollector-elasticsearch_5-lib noarch 2.6.0.1-1        /streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch
                                                                                                        16 M
 streamsets-datacollector-groovy_2_4-lib      noarch 2.6.0.1-1        /streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch
                                                                                                        17 M
 streamsets-datacollector-hdp_2_2-lib         noarch 2.6.0.1-1        /streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch
                                                                                                       133 M
 streamsets-datacollector-hdp_2_3-lib         noarch 2.6.0.1-1        /streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch
                                                                                                       152 M
 streamsets-datacollector-hdp_2_4-lib         noarch 2.6.0.1-1        /streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch
                                                                                                       156 M
 streamsets-datacollector-hdp_2_5-lib         noarch 2.6.0.1-1        /streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch
                                                                                                       161 M
 streamsets-datacollector-hdp_2_6-lib         noarch 2.6.0.1-1        /streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch
                                                                                                       162 M
 streamsets-datacollector-influxdb_0_9-lib    noarch 2.6.0.1-1        /streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch
                                                                                                        13 M
 streamsets-datacollector-jdbc-lib            noarch 2.6.0.1-1        /streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch
                                                                                                        14 M
 streamsets-datacollector-jms-lib             noarch 2.6.0.1-1        /streamsets-datacollector-jms-lib-2.6.0.1-1.noarch
                                                                                                        15 M
 streamsets-datacollector-jython_2_7-lib      noarch 2.6.0.1-1        /streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch
                                                                                                        47 M
 streamsets-datacollector-mapr_5_0-lib        noarch 2.6.0.1-1        /streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch
                                                                                                        14 M
 streamsets-datacollector-mapr_5_1-lib        noarch 2.6.0.1-1        /streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch
                                                                                                        54 M
 streamsets-datacollector-mapr_5_2-lib        noarch 2.6.0.1-1        /streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch
                                                                                                       105 M
 streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib
                                              noarch 2.6.0.1-1        /streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch
                                                                                                       151 M
 streamsets-datacollector-mongodb_3-lib       noarch 2.6.0.1-1        /streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch
                                                                                                        14 M
 streamsets-datacollector-mysql-binlog-lib    noarch 2.6.0.1-1        /streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch
                                                                                                        14 M
 streamsets-datacollector-omniture-lib        noarch 2.6.0.1-1        /streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch
                                                                                                        13 M
 streamsets-datacollector-rabbitmq-lib        noarch 2.6.0.1-1        /streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch
                                                                                                        14 M
 streamsets-datacollector-redis-lib           noarch 2.6.0.1-1        /streamsets-datacollector-redis-lib-2.6.0.1-1.noarch
                                                                                                        13 M
 streamsets-datacollector-salesforce-lib      noarch 2.6.0.1-1        /streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch
                                                                                                        18 M
 streamsets-datacollector-stats-lib           noarch 2.6.0.1-1        /streamsets-datacollector-stats-lib-2.6.0.1-1.noarch
                                                                                                        30 M
Installing for dependencies:
 alsa-lib                                     x86_64 1.1.1-1.el7      rhui-REGION-rhel-server-releases 415 k
 copy-jdk-configs                             noarch 1.2-1.el7        rhui-REGION-rhel-server-releases  14 k
 fontconfig                                   x86_64 2.10.95-10.el7   rhui-REGION-rhel-server-releases 229 k
 fontpackages-filesystem                      noarch 1.44-8.el7       rhui-REGION-rhel-server-releases 9.9 k
 giflib                                       x86_64 4.1.6-9.el7      rhui-REGION-rhel-server-releases  40 k
 java-1.8.0-openjdk                           x86_64 1:1.8.0.131-3.b12.el7_3
                                                                      rhui-REGION-rhel-server-releases 233 k
 java-1.8.0-openjdk-headless                  x86_64 1:1.8.0.131-3.b12.el7_3
                                                                      rhui-REGION-rhel-server-releases  31 M
 javapackages-tools                           noarch 3.4.1-11.el7     rhui-REGION-rhel-server-releases  73 k
 libICE                                       x86_64 1.0.9-2.el7      rhui-REGION-rhel-server-releases  65 k
 libSM                                        x86_64 1.2.2-2.el7      rhui-REGION-rhel-server-releases  39 k
 libX11                                       x86_64 1.6.3-3.el7      rhui-REGION-rhel-server-releases 606 k
 libX11-common                                noarch 1.6.3-3.el7      rhui-REGION-rhel-server-releases 162 k
 libXau                                       x86_64 1.0.8-2.1.el7    rhui-REGION-rhel-server-releases  29 k
 libXcomposite                                x86_64 0.4.4-4.1.el7    rhui-REGION-rhel-server-releases  22 k
 libXext                                      x86_64 1.3.3-3.el7      rhui-REGION-rhel-server-releases  39 k
 libXfont                                     x86_64 1.5.1-2.el7      rhui-REGION-rhel-server-releases 150 k
 libXi                                        x86_64 1.7.4-2.el7      rhui-REGION-rhel-server-releases  40 k
 libXrender                                   x86_64 0.9.8-2.1.el7    rhui-REGION-rhel-server-releases  26 k
 libXtst                                      x86_64 1.2.2-2.1.el7    rhui-REGION-rhel-server-releases  20 k
 libfontenc                                   x86_64 1.1.2-3.el7      rhui-REGION-rhel-server-releases  30 k
 libjpeg-turbo                                x86_64 1.2.90-5.el7     rhui-REGION-rhel-server-releases 134 k
 libpng                                       x86_64 2:1.5.13-7.el7_2 rhui-REGION-rhel-server-releases 213 k
 libxcb                                       x86_64 1.11-4.el7       rhui-REGION-rhel-server-releases 189 k
 lksctp-tools                                 x86_64 1.0.17-2.el7     rhui-REGION-rhel-server-releases  88 k
 python-javapackages                          noarch 3.4.1-11.el7     rhui-REGION-rhel-server-releases  31 k
 ttmkfdir                                     x86_64 3.0.9-42.el7     rhui-REGION-rhel-server-releases  48 k
 tzdata-java                                  noarch 2017b-1.el7      rhui-REGION-rhel-server-releases 182 k
 xorg-x11-font-utils                          x86_64 1:7.5-20.el7     rhui-REGION-rhel-server-releases  87 k
 xorg-x11-fonts-Type1                         noarch 7.5-9.el7        rhui-REGION-rhel-server-releases 521 k
Updating for dependencies:
 chkconfig                                    x86_64 1.7.2-1.el7_3.1  rhui-REGION-rhel-server-releases 175 k
 nspr                                         x86_64 4.13.1-1.0.el7_3 rhui-REGION-rhel-server-releases 126 k
 nss                                          x86_64 3.28.4-1.2.el7_3 rhui-REGION-rhel-server-releases 872 k
 nss-sysinit                                  x86_64 3.28.4-1.2.el7_3 rhui-REGION-rhel-server-releases  58 k
 nss-tools                                    x86_64 3.28.4-1.2.el7_3 rhui-REGION-rhel-server-releases 496 k
 nss-util                                     x86_64 3.28.4-1.0.el7_3 rhui-REGION-rhel-server-releases  73 k

Transaction Summary
=============================================================================================================
Install  59 Packages (+29 Dependent packages)
Upgrade              (  6 Dependent packages)

Total size: 3.8 G
Total download size: 37 M
Is this ok [y/d/N]: y
Downloading packages:
Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
(1/35): alsa-lib-1.1.1-1.el7.x86_64.rpm                                               | 415 kB  00:00:00
(2/35): copy-jdk-configs-1.2-1.el7.noarch.rpm                                         |  14 kB  00:00:00
(3/35): fontconfig-2.10.95-10.el7.x86_64.rpm                                          | 229 kB  00:00:00
(4/35): fontpackages-filesystem-1.44-8.el7.noarch.rpm                                 | 9.9 kB  00:00:00
(5/35): chkconfig-1.7.2-1.el7_3.1.x86_64.rpm                                          | 175 kB  00:00:00
(6/35): giflib-4.1.6-9.el7.x86_64.rpm                                                 |  40 kB  00:00:00
(7/35): java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64.rpm                           | 233 kB  00:00:00
(8/35): javapackages-tools-3.4.1-11.el7.noarch.rpm                                    |  73 kB  00:00:00
(9/35): libICE-1.0.9-2.el7.x86_64.rpm                                                 |  65 kB  00:00:00
(10/35): libSM-1.2.2-2.el7.x86_64.rpm                                                 |  39 kB  00:00:00
(11/35): libX11-1.6.3-3.el7.x86_64.rpm                                                | 606 kB  00:00:00
(12/35): libX11-common-1.6.3-3.el7.noarch.rpm                                         | 162 kB  00:00:00
(13/35): libXau-1.0.8-2.1.el7.x86_64.rpm                                              |  29 kB  00:00:00
(14/35): libXcomposite-0.4.4-4.1.el7.x86_64.rpm                                       |  22 kB  00:00:00
(15/35): libXext-1.3.3-3.el7.x86_64.rpm                                               |  39 kB  00:00:00
(16/35): java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64.rpm                 |  31 MB  00:00:00
(17/35): libXfont-1.5.1-2.el7.x86_64.rpm                                              | 150 kB  00:00:00
(18/35): libXi-1.7.4-2.el7.x86_64.rpm                                                 |  40 kB  00:00:00
(19/35): libXrender-0.9.8-2.1.el7.x86_64.rpm                                          |  26 kB  00:00:00
(20/35): libXtst-1.2.2-2.1.el7.x86_64.rpm                                             |  20 kB  00:00:00
(21/35): libfontenc-1.1.2-3.el7.x86_64.rpm                                            |  30 kB  00:00:00
(22/35): libxcb-1.11-4.el7.x86_64.rpm                                                 | 189 kB  00:00:00
(23/35): libjpeg-turbo-1.2.90-5.el7.x86_64.rpm                                        | 134 kB  00:00:00
(24/35): libpng-1.5.13-7.el7_2.x86_64.rpm                                             | 213 kB  00:00:00
(25/35): lksctp-tools-1.0.17-2.el7.x86_64.rpm                                         |  88 kB  00:00:00
(26/35): nspr-4.13.1-1.0.el7_3.x86_64.rpm                                             | 126 kB  00:00:00
(27/35): nss-3.28.4-1.2.el7_3.x86_64.rpm                                              | 872 kB  00:00:00
(28/35): nss-sysinit-3.28.4-1.2.el7_3.x86_64.rpm                                      |  58 kB  00:00:00
(29/35): nss-tools-3.28.4-1.2.el7_3.x86_64.rpm                                        | 496 kB  00:00:00
(30/35): nss-util-3.28.4-1.0.el7_3.x86_64.rpm                                         |  73 kB  00:00:00
(31/35): python-javapackages-3.4.1-11.el7.noarch.rpm                                  |  31 kB  00:00:00
(32/35): ttmkfdir-3.0.9-42.el7.x86_64.rpm                                             |  48 kB  00:00:00
(33/35): tzdata-java-2017b-1.el7.noarch.rpm                                           | 182 kB  00:00:00
(34/35): xorg-x11-font-utils-7.5-20.el7.x86_64.rpm                                    |  87 kB  00:00:00
(35/35): xorg-x11-fonts-Type1-7.5-9.el7.noarch.rpm                                    | 521 kB  00:00:00
-------------------------------------------------------------------------------------------------------------
Total                                                                         28 MB/s |  37 MB  00:00:01
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : nspr-4.13.1-1.0.el7_3.x86_64                                                            1/100
  Updating   : nss-util-3.28.4-1.0.el7_3.x86_64                                                        2/100
  Updating   : chkconfig-1.7.2-1.el7_3.1.x86_64                                                        3/100
  Updating   : nss-3.28.4-1.2.el7_3.x86_64                                                             4/100
  Updating   : nss-sysinit-3.28.4-1.2.el7_3.x86_64                                                     5/100
  Installing : libICE-1.0.9-2.el7.x86_64                                                               6/100
  Installing : libjpeg-turbo-1.2.90-5.el7.x86_64                                                       7/100
  Installing : libfontenc-1.1.2-3.el7.x86_64                                                           8/100
  Installing : libXfont-1.5.1-2.el7.x86_64                                                             9/100
  Installing : 1:xorg-x11-font-utils-7.5-20.el7.x86_64                                                10/100
  Installing : libSM-1.2.2-2.el7.x86_64                                                               11/100
  Installing : copy-jdk-configs-1.2-1.el7.noarch                                                      12/100
  Installing : alsa-lib-1.1.1-1.el7.x86_64                                                            13/100
  Installing : tzdata-java-2017b-1.el7.noarch                                                         14/100
  Installing : ttmkfdir-3.0.9-42.el7.x86_64                                                           15/100
  Installing : fontpackages-filesystem-1.44-8.el7.noarch                                              16/100
  Installing : fontconfig-2.10.95-10.el7.x86_64                                                       17/100
  Installing : xorg-x11-fonts-Type1-7.5-9.el7.noarch                                                  18/100
  Installing : libX11-common-1.6.3-3.el7.noarch                                                       19/100
  Installing : libXau-1.0.8-2.1.el7.x86_64                                                            20/100
  Installing : libxcb-1.11-4.el7.x86_64                                                               21/100
  Installing : libX11-1.6.3-3.el7.x86_64                                                              22/100
  Installing : libXext-1.3.3-3.el7.x86_64                                                             23/100
  Installing : libXi-1.7.4-2.el7.x86_64                                                               24/100
  Installing : libXtst-1.2.2-2.1.el7.x86_64                                                           25/100
  Installing : libXcomposite-0.4.4-4.1.el7.x86_64                                                     26/100
  Installing : giflib-4.1.6-9.el7.x86_64                                                              27/100
  Installing : libXrender-0.9.8-2.1.el7.x86_64                                                        28/100
  Installing : lksctp-tools-1.0.17-2.el7.x86_64                                                       29/100
  Installing : python-javapackages-3.4.1-11.el7.noarch                                                30/100
  Installing : javapackages-tools-3.4.1-11.el7.noarch                                                 31/100
  Installing : 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64                             32/100
  Installing : 2:libpng-1.5.13-7.el7_2.x86_64                                                         33/100
  Installing : 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64                                      34/100
  Installing : streamsets-datacollector-2.6.0.1-1.noarch                                              35/100
  Installing : streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch                                 36/100
  Installing : streamsets-datacollector-jms-lib-2.6.0.1-1.noarch                                      37/100
  Installing : streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch                          38/100
  Installing : streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch                               39/100
  Installing : streamsets-datacollector-redis-lib-2.6.0.1-1.noarch                                    40/100
  Installing : streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch                                41/100
  Installing : streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch            42/100
  Installing : streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch                                  43/100
  Installing : streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch                          44/100
  Installing : streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch                        45/100
  Installing : streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            46/100
  Installing : streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch                                  47/100
  Installing : streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch                              48/100
  Installing : streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch                             49/100
  Installing : streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch                         50/100
  Installing : streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch                                 51/100
  Installing : streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch                                 52/100
  Installing : streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch                               53/100
  Installing : streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch                            54/100
  Installing : streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch                   55/100
  Installing : streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch            56/100
  Installing : streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch                                  57/100
  Installing : streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch                       58/100
  Installing : streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch            59/100
  Installing : streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch                                 60/100
  Installing : streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch                                  61/100
  Installing : streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch                                  62/100
  Installing : streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch                                  63/100
  Installing : streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch                          64/100
  Installing : streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch                        65/100
  Installing : streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch                                 66/100
  Installing : streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch                                 67/100
  Installing : streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch                                  68/100
  Installing : streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch                               69/100
  Installing : streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            70/100
  Installing : streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch           71/100
  Installing : streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch           72/100
  Installing : streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch                         73/100
  Installing : streamsets-datacollector-basic-lib-2.6.0.1-1.noarch                                    74/100
  Installing : streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch                                  75/100
  Installing : streamsets-datacollector-azure-lib-2.6.0.1-1.noarch                                    76/100
  Installing : streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch                                 77/100
  Installing : streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch                                  78/100
  Installing : streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch                            79/100
  Installing : streamsets-datacollector-aws-lib-2.6.0.1-1.noarch                                      80/100
  Installing : streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch                            81/100
  Installing : streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch                                  82/100
  Installing : streamsets-datacollector-stats-lib-2.6.0.1-1.noarch                                    83/100
  Installing : streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch                                 84/100
  Installing : streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch                       85/100
  Installing : streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch                                     86/100
  Installing : streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch                            87/100
  Installing : streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch                          88/100
  Installing : streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch                          89/100
  Installing : streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch                                  90/100
  Installing : streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch                             91/100
  Installing : streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            92/100
  Installing : streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch                                  93/100
  Updating   : nss-tools-3.28.4-1.2.el7_3.x86_64                                                      94/100
  Cleanup    : nss-tools-3.21.0-9.el7_2.x86_64                                                        95/100
  Cleanup    : nss-sysinit-3.21.0-9.el7_2.x86_64                                                      96/100
  Cleanup    : nss-3.21.0-9.el7_2.x86_64                                                              97/100
  Cleanup    : nss-util-3.21.0-2.2.el7_2.x86_64                                                       98/100
  Cleanup    : nspr-4.11.0-1.el7_2.x86_64                                                             99/100
  Cleanup    : chkconfig-1.3.61-5.el7_2.1.x86_64                                                     100/100
  Verifying  : libXext-1.3.3-3.el7.x86_64                                                              1/100
  Verifying  : streamsets-datacollector-cdh_5_10-lib-2.6.0.1-1.noarch                                  2/100
  Verifying  : nspr-4.13.1-1.0.el7_3.x86_64                                                            3/100
  Verifying  : nss-3.28.4-1.2.el7_3.x86_64                                                             4/100
  Verifying  : libXtst-1.2.2-2.1.el7.x86_64                                                            5/100
  Verifying  : streamsets-datacollector-jms-lib-2.6.0.1-1.noarch                                       6/100
  Verifying  : streamsets-datacollector-elasticsearch_5-lib-2.6.0.1-1.noarch                           7/100
  Verifying  : streamsets-datacollector-jython_2_7-lib-2.6.0.1-1.noarch                                8/100
  Verifying  : 2:libpng-1.5.13-7.el7_2.x86_64                                                          9/100
  Verifying  : streamsets-datacollector-redis-lib-2.6.0.1-1.noarch                                    10/100
  Verifying  : streamsets-datacollector-mongodb_3-lib-2.6.0.1-1.noarch                                11/100
  Verifying  : nss-util-3.28.4-1.0.el7_3.x86_64                                                       12/100
  Verifying  : streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib-2.6.0.1-1.noarch            13/100
  Verifying  : python-javapackages-3.4.1-11.el7.noarch                                                14/100
  Verifying  : libXcomposite-0.4.4-4.1.el7.x86_64                                                     15/100
  Verifying  : streamsets-datacollector-cdh_5_7-lib-2.6.0.1-1.noarch                                  16/100
  Verifying  : streamsets-datacollector-apache-kudu_1_3-lib-2.6.0.1-1.noarch                          17/100
  Verifying  : lksctp-tools-1.0.17-2.el7.x86_64                                                       18/100
  Verifying  : streamsets-datacollector-apache-kafka_0_10-lib-2.6.0.1-1.noarch                        19/100
  Verifying  : streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            20/100
  Verifying  : streamsets-datacollector-hdp_2_3-lib-2.6.0.1-1.noarch                                  21/100
  Verifying  : streamsets-datacollector-cassandra_3-lib-2.6.0.1-1.noarch                              22/100
  Verifying  : libXau-1.0.8-2.1.el7.x86_64                                                            23/100
  Verifying  : streamsets-datacollector-mysql-binlog-lib-2.6.0.1-1.noarch                             24/100
  Verifying  : libX11-1.6.3-3.el7.x86_64                                                              25/100
  Verifying  : streamsets-datacollector-cdh_spark_2_1_r1-lib-2.6.0.1-1.noarch                         26/100
  Verifying  : 1:xorg-x11-font-utils-7.5-20.el7.x86_64                                                27/100
  Verifying  : streamsets-datacollector-cdh_5_11-lib-2.6.0.1-1.noarch                                 28/100
  Verifying  : libfontenc-1.1.2-3.el7.x86_64                                                          29/100
  Verifying  : libxcb-1.11-4.el7.x86_64                                                               30/100
  Verifying  : streamsets-datacollector-rabbitmq-lib-2.6.0.1-1.noarch                                 31/100
  Verifying  : streamsets-datacollector-salesforce-lib-2.6.0.1-1.noarch                               32/100
  Verifying  : streamsets-datacollector-cdh_kafka_2_0-lib-2.6.0.1-1.noarch                            33/100
  Verifying  : streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib-2.6.0.1-1.noarch                   34/100
  Verifying  : streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch            35/100
  Verifying  : streamsets-datacollector-cdh_5_8-lib-2.6.0.1-1.noarch                                  36/100
  Verifying  : streamsets-datacollector-apache-kafka_0_8_2-lib-2.6.0.1-1.noarch                       37/100
  Verifying  : streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib-2.6.0.1-1.noarch            38/100
  Verifying  : streamsets-datacollector-mapr_5_0-lib-2.6.0.1-1.noarch                                 39/100
  Verifying  : 1:java-1.8.0-openjdk-headless-1.8.0.131-3.b12.el7_3.x86_64                             40/100
  Verifying  : streamsets-datacollector-cdh_5_3-lib-2.6.0.1-1.noarch                                  41/100
  Verifying  : javapackages-tools-3.4.1-11.el7.noarch                                                 42/100
  Verifying  : streamsets-datacollector-cdh_5_9-lib-2.6.0.1-1.noarch                                  43/100
  Verifying  : libXi-1.7.4-2.el7.x86_64                                                               44/100
  Verifying  : streamsets-datacollector-cdh_5_2-lib-2.6.0.1-1.noarch                                  45/100
  Verifying  : libX11-common-1.6.3-3.el7.noarch                                                       46/100
  Verifying  : streamsets-datacollector-apache-kudu_1_1-lib-2.6.0.1-1.noarch                          47/100
  Verifying  : fontconfig-2.10.95-10.el7.x86_64                                                       48/100
  Verifying  : streamsets-datacollector-apache-solr_6_1_0-lib-2.6.0.1-1.noarch                        49/100
  Verifying  : nss-tools-3.28.4-1.2.el7_3.x86_64                                                      50/100
  Verifying  : libjpeg-turbo-1.2.90-5.el7.x86_64                                                      51/100
  Verifying  : fontpackages-filesystem-1.44-8.el7.noarch                                              52/100
  Verifying  : ttmkfdir-3.0.9-42.el7.x86_64                                                           53/100
  Verifying  : streamsets-datacollector-omniture-lib-2.6.0.1-1.noarch                                 54/100
  Verifying  : giflib-4.1.6-9.el7.x86_64                                                              55/100
  Verifying  : streamsets-datacollector-bigtable-lib-2.6.0.1-1.noarch                                 56/100
  Verifying  : streamsets-datacollector-hdp_2_5-lib-2.6.0.1-1.noarch                                  57/100
  Verifying  : streamsets-datacollector-groovy_2_4-lib-2.6.0.1-1.noarch                               58/100
  Verifying  : streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            59/100
  Verifying  : tzdata-java-2017b-1.el7.noarch                                                         60/100
  Verifying  : streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch           61/100
  Verifying  : libICE-1.0.9-2.el7.x86_64                                                              62/100
  Verifying  : streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib-2.6.0.1-1.noarch           63/100
  Verifying  : streamsets-datacollector-apache-kafka_0_9-lib-2.6.0.1-1.noarch                         64/100
  Verifying  : libXrender-0.9.8-2.1.el7.x86_64                                                        65/100
  Verifying  : streamsets-datacollector-basic-lib-2.6.0.1-1.noarch                                    66/100
  Verifying  : 1:java-1.8.0-openjdk-1.8.0.131-3.b12.el7_3.x86_64                                      67/100
  Verifying  : streamsets-datacollector-cdh_5_5-lib-2.6.0.1-1.noarch                                  68/100
  Verifying  : streamsets-datacollector-azure-lib-2.6.0.1-1.noarch                                    69/100
  Verifying  : libSM-1.2.2-2.el7.x86_64                                                               70/100
  Verifying  : alsa-lib-1.1.1-1.el7.x86_64                                                            71/100
  Verifying  : streamsets-datacollector-mapr_5_2-lib-2.6.0.1-1.noarch                                 72/100
  Verifying  : streamsets-datacollector-cdh_5_4-lib-2.6.0.1-1.noarch                                  73/100
  Verifying  : streamsets-datacollector-cdh_kafka_1_2-lib-2.6.0.1-1.noarch                            74/100
  Verifying  : streamsets-datacollector-aws-lib-2.6.0.1-1.noarch                                      75/100
  Verifying  : streamsets-datacollector-cdh_kafka_2_1-lib-2.6.0.1-1.noarch                            76/100
  Verifying  : streamsets-datacollector-hdp_2_4-lib-2.6.0.1-1.noarch                                  77/100
  Verifying  : streamsets-datacollector-stats-lib-2.6.0.1-1.noarch                                    78/100
  Verifying  : streamsets-datacollector-mapr_5_1-lib-2.6.0.1-1.noarch                                 79/100
  Verifying  : streamsets-datacollector-apache-kafka_0_8_1-lib-2.6.0.1-1.noarch                       80/100
  Verifying  : streamsets-datacollector-2.6.0.1-1.noarch                                              81/100
  Verifying  : streamsets-datacollector-jdbc-lib-2.6.0.1-1.noarch                                     82/100
  Verifying  : chkconfig-1.7.2-1.el7_3.1.x86_64                                                       83/100
  Verifying  : streamsets-datacollector-cdh_kafka_1_3-lib-2.6.0.1-1.noarch                            84/100
  Verifying  : streamsets-datacollector-apache-kudu_1_0-lib-2.6.0.1-1.noarch                          85/100
  Verifying  : streamsets-datacollector-apache-kudu_1_2-lib-2.6.0.1-1.noarch                          86/100
  Verifying  : copy-jdk-configs-1.2-1.el7.noarch                                                      87/100
  Verifying  : nss-sysinit-3.28.4-1.2.el7_3.x86_64                                                    88/100
  Verifying  : streamsets-datacollector-hdp_2_2-lib-2.6.0.1-1.noarch                                  89/100
  Verifying  : xorg-x11-fonts-Type1-7.5-9.el7.noarch                                                  90/100
  Verifying  : streamsets-datacollector-influxdb_0_9-lib-2.6.0.1-1.noarch                             91/100
  Verifying  : libXfont-1.5.1-2.el7.x86_64                                                            92/100
  Verifying  : streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib-2.6.0.1-1.noarch            93/100
  Verifying  : streamsets-datacollector-hdp_2_6-lib-2.6.0.1-1.noarch                                  94/100
  Verifying  : nspr-4.11.0-1.el7_2.x86_64                                                             95/100
  Verifying  : nss-tools-3.21.0-9.el7_2.x86_64                                                        96/100
  Verifying  : nss-util-3.21.0-2.2.el7_2.x86_64                                                       97/100
  Verifying  : chkconfig-1.3.61-5.el7_2.1.x86_64                                                      98/100
  Verifying  : nss-3.21.0-9.el7_2.x86_64                                                              99/100
  Verifying  : nss-sysinit-3.21.0-9.el7_2.x86_64                                                     100/100

Installed:
  streamsets-datacollector.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kafka_0_10-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kafka_0_8_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kafka_0_8_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kafka_0_9-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kudu_1_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kudu_1_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kudu_1_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-kudu_1_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-apache-solr_6_1_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-aws-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-azure-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-basic-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-bigtable-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cassandra_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_10-cluster-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_10-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_11-cluster-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_11-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_4-cluster-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_4-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_5-cluster-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_5-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_7-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_7-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_8-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_8-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_9-cluster-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_5_9-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_kafka_1_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_kafka_1_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_kafka_2_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_kafka_2_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-cdh_spark_2_1_r1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-elasticsearch_5-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-groovy_2_4-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-hdp_2_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-hdp_2_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-hdp_2_4-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-hdp_2_5-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-hdp_2_6-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-influxdb_0_9-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-jdbc-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-jms-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-jython_2_7-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mapr_5_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mapr_5_1-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mapr_5_2-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mapr_spark_2_1_mep_3_0-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mongodb_3-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-mysql-binlog-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-omniture-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-rabbitmq-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-redis-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-salesforce-lib.noarch 0:2.6.0.1-1
  streamsets-datacollector-stats-lib.noarch 0:2.6.0.1-1

Dependency Installed:
  alsa-lib.x86_64 0:1.1.1-1.el7
  copy-jdk-configs.noarch 0:1.2-1.el7
  fontconfig.x86_64 0:2.10.95-10.el7
  fontpackages-filesystem.noarch 0:1.44-8.el7
  giflib.x86_64 0:4.1.6-9.el7
  java-1.8.0-openjdk.x86_64 1:1.8.0.131-3.b12.el7_3
  java-1.8.0-openjdk-headless.x86_64 1:1.8.0.131-3.b12.el7_3
  javapackages-tools.noarch 0:3.4.1-11.el7
  libICE.x86_64 0:1.0.9-2.el7
  libSM.x86_64 0:1.2.2-2.el7
  libX11.x86_64 0:1.6.3-3.el7
  libX11-common.noarch 0:1.6.3-3.el7
  libXau.x86_64 0:1.0.8-2.1.el7
  libXcomposite.x86_64 0:0.4.4-4.1.el7
  libXext.x86_64 0:1.3.3-3.el7
  libXfont.x86_64 0:1.5.1-2.el7
  libXi.x86_64 0:1.7.4-2.el7
  libXrender.x86_64 0:0.9.8-2.1.el7
  libXtst.x86_64 0:1.2.2-2.1.el7
  libfontenc.x86_64 0:1.1.2-3.el7
  libjpeg-turbo.x86_64 0:1.2.90-5.el7
  libpng.x86_64 2:1.5.13-7.el7_2
  libxcb.x86_64 0:1.11-4.el7
  lksctp-tools.x86_64 0:1.0.17-2.el7
  python-javapackages.noarch 0:3.4.1-11.el7
  ttmkfdir.x86_64 0:3.0.9-42.el7
  tzdata-java.noarch 0:2017b-1.el7
  xorg-x11-font-utils.x86_64 1:7.5-20.el7
  xorg-x11-fonts-Type1.noarch 0:7.5-9.el7

Dependency Updated:
  chkconfig.x86_64 0:1.7.2-1.el7_3.1                   nspr.x86_64 0:4.13.1-1.0.el7_3
  nss.x86_64 0:3.28.4-1.2.el7_3                        nss-sysinit.x86_64 0:3.28.4-1.2.el7_3
  nss-tools.x86_64 0:3.28.4-1.2.el7_3                  nss-util.x86_64 0:3.28.4-1.0.el7_3

Complete!
[ec2-user@ip-172-31-32-134 streamsets-datacollector-2.6.0.1-all-rpms]$


Start streamsets:
service sdc start





```
