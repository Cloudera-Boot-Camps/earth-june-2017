# Ingestion using sqoop

We were able to create an oozie workflow using hue.
The full oozie workflow is [here](workflow.json) and just the oozie xml
is [here](workflow.xml). Hue + oozie + sqoop was quite difficult to setup.

Running the oozie job from the shell was done by exporting the workflow.xml
out and referencing it from a [shell script](submit_from_shell.md).

Additionally transforations were done using [hive](hive_table.hql).
