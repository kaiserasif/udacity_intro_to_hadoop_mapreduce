# Udacity - Introduction to Hadoop and MapReduce

All are done in cloudera hadoop image.
To transfer files ifconfig in cloudera, use that ip training@ip, pass training.

To run using cloudera alias:
hs mapper.py reducer.py data_path/in/hadoop output/to_create/in/hadoop

To retrive result:
hadoop fs -get output/to_create/in/hadoop path/in/local/filesystem

Other commands:
hadoop fs -put localfile hadooppath
hadoop fs -ls
hadoop fs -mkdir
