# distributed-system
distributed-system-project, mqtt-kafka-smartHome

# build 
pip install paho-mqtt
pip install kafka

# docker mqtt
unzip mosquitto.7z
docker-compose -f docker-compose.yml up --build


# docker kafka

unzip kafka.7z
# create network
docker network create \
  --driver=bridge \
  --subnet=172.28.0.0/16 \
  --gateway=172.28.0.1 \
  dev

docker-compose up -d 