#Start Zookeeper
(Be on the correct path file)
bin\windows\zookeeper-server-start.bat config\zookeeper.properties

#Start kafka server (broker)
bin\windows\kafka-server-start.bat E:\kafka\config\server.properties

# create a topic
bin\windows\kafka-topics.bat --create --topic data-quality --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

##verify topic
bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

#Run producer
python producer.py
# Run consumer
python consumer.py
