# distributed-system
distributed-system-project, mqtt-kafka-smartHome

# build 
pip install paho-mqtt
pip install kafka

# docker mqtt
broker1/docker-compose -f docker-compose.yml up --build
broker2/docker-compose -f docker-compose.yml up --build
broker3/docker-compose -f docker-compose.yml up --build

# docker kafka
kafka/docker-compose -f docker-compose.yml up --build

# create network
docker network create \
  --driver=bridge \
  --subnet=172.28.0.0/16 \
  --gateway=172.28.0.1 \
  dev

# start simulation scripts
python3 main_simulation1.py
python3 main_simulation2.py
python3 main_simulation3.py

# run server
python3 main1.py
python3 main2.py
python3 main3.py

# run node-red

run node-red and import the flows.json
