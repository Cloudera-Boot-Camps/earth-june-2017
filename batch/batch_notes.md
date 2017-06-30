* sometimes you have rows that are updated, so you can't fetch incrementally
* you have to fetch either:
  * ALL the rows
  * figure out which rows changed and grab those

* how common do you run your (sqoop) batch jobs?
  * a very common thing is once a day. perhaps at end of business day
    * of course this means your data gets stale
    * but the more frequently you run, (interday syncs) makes things
      much more difficult
    * if you're modifying data while users are accessing it, things
      gets hairer
    * the tighter your frequency the harder it gets. especially, it becomes
      less fault tolerant. you could even have jobs backed up

* sometimes you have dependency graphs. say you want to:
  * fetch two tables simultaneously.
  * convert data types of the two tables (simultaneously)
  * then denormalize the tables together
  * this is an oozie work flow

* oozie is great for these complex batch jobs dependency graphs
  * each vertex is an action
  * oozie is tricky and poorly documented!

* you can also have a sub workflow action types
  * basically a template of a commonly performed action
  * modularity, like a function within the workflow

* oozie coordinators are schedulers for when to run jobs
  * but it's simplistic
  * if you have multiple dependencies for when the job runs, it
    sucks at this.
  * if you have a complex scheduling conditions, use an enterprise
    coordinator like control-m/autosys

* a good rule of thumb:
  * make sure your oozie job does cleanup before running, in case
    a previous job failed and left things tmp files etc. in a half
    state
* with failures, you can restart from the failed action, instead of
  having to to rerun from the beginning

* most common sql engine for transforms is hive
* sarting to become more popular now is spark sql:
  * better performance
  * it starts to suplament oozie at some point, because it is a
    general purpose language.
  * if you use spark instead of hive + oozie, your DAG is in spark

* you **COULD** use impala for ETL, but not a good idea
  * not fault tolerant
  * few file formats
  * slower writes
  * no oozie action types

* spark
  * actions are writes, displays to users etc.
  * transformations are ... all the other stuff, side effect free

* two spark APIs:
  * RDD
  * dataset/dataframe -> structured data meant really for sql
    * you could of course run other structured things on it

* hive doesn't actually run queries, so you can switch MR2 for spark
  * hive metastore holds metadata for all sql engines
    * holds all the tables and views
    * but it can also be used by impala and others
    * centralized metadata store
    * not the most efficiently built service...
  * hiveserver2 required for **sentry**
    * submit jobs to hiveserver2 and it determines whether to use
      mapreduce or spark
  * hive on spark uses the RDD api.
  * generally speaking hive on spark is going to be slower then
    spark sql
vf
