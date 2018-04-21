# Udacity - Introduction to Hadoop and MapReduce

All are done in cloudera hadoop image.<br>
To transfer files ifconfig in cloudera, use that ip training@ip, pass training.<br>

To run using cloudera alias:<br>
hs mapper.py reducer.py data_path/in/hadoop output/to_create/in/hadoop<br>

To retrive result:<br>
hadoop fs -get output/to_create/in/hadoop path/in/local/filesystem<br>

Other commands:<br>
hadoop fs -put localfile hadooppath<br>
hadoop fs -ls<br>
hadoop fs -mkdir<br>
