import json
import traceback

from kafka import KafkaProducer
from kafka.errors import kafka_errors


class ProducerKafka:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            security_protocol="PLAINTEXT",

            bootstrap_servers=bootstrap_servers,
            key_serializer=lambda k: json.dumps(k).encode(),
            value_serializer=lambda v: json.dumps(v).encode())

    def send(self, topic, key, msg):
        future = self.producer.send(
            topic,
            key=key,
            value=msg,
            partition=0)
        print("send {}".format(msg))
        try:
            future.get(timeout=10)  # monitor publish
        except kafka_errors:  # fail throws kafka_errors
            traceback.format_exc()
