# kafkatask1
Run the following command to setup the environment
Clone the repository

git clone https://github.com/dladysas/kafkatask1.git
cd kafkatask1

Start the environment

docker-compose up -d

Images will start on the following ports
ZooKeeper on port 2181
Kafka on port 9092
KSQL Server on port 8088

Verify Services

docker ps

Access KSQL CLI

docker exec -it <ksqldb-cli-container-name> ksql http://ksqldb-server:8088

