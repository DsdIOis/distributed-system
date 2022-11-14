import json

from kafka import KafkaConsumer


def consumer_demo():
    consumer = KafkaConsumer(
        'kafka_demo',
        security_protocol="PLAINTEXT",
        bootstrap_servers=[
            'localhost:9093',
            'localhost:9094',
            'localhost:9095'
        ],
    )
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
        )
        )


if __name__ == '__main__':
    consumer_demo()

