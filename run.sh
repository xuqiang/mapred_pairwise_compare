#!/bin/bash

export HADOOP_HOME=/home/resys/var/hadoop-1.1.2/
OUTPUT=hdfs:///tmp/output/
INPUT=hdfs:///tmp/input/

$HADOOP_HOME/bin/hadoop fs -rmr ${OUTPUT}
python pairwise.py -r hadoop \
	--output-dir=$OUTPUT $INPUT  \
	--jobconf "mapred.job.map.capacity=500"	\
	--jobconf "mapred.job.reduce.capacity=100"	\
	--jobconf "mapred.map.tasks=500"	\
	--jobconf "mapred.reduce.tasks=100"	\
	--jobconf "total=4"	\
	-v \
	--no-output

echo "done"
exit 0;
