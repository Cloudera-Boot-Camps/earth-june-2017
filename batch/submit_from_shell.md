```
sudo -u hdfs oozie job --oozie http://localhost:11000/oozie -config /tmp/oozie_conf.xml -run
```

#oozie_conf.xml
```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<configuration>
<property>
        <name>nameNode</name>
        <value>hdfs://ip-172-31-47-126.us-west-2.compute.internal:8020</value>
</property>
<property>
        <name>jobTracker</name>
        <value>ip-172-31-47-126.us-west-2.compute.internal:8032</value>
</property>
<property>
        <name>oozie.wf.application.path</name>
        <value>/user/hdfs/workflow.xml</value>
</property>
<property>
	<name>oozie.use.system.libpath</name>
	<value>true</value>
</property>
</configuration>
```
