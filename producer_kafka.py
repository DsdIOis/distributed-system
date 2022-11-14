import json
import traceback

from kafka import KafkaProducer
from kafka.errors import kafka_errors


def producer_demo():
    producer = KafkaProducer(
        security_protocol="PLAINTEXT",
        bootstrap_servers=[
            'localhost:9093',
            'localhost:9094',
            'localhost:9095'
        ],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    # 发送三条消息
    for i in range(0, 3):
        future = producer.send(
            'kafka_demo',
            key='count_num',
            value=str(i),
            partition=0)
        print("send {}".format(str(i)))
        try:
            future.get(timeout=10)  # 监控是否发送成功
        except kafka_errors:  # 发送失败抛出kafka_errors
            traceback.format_exc()


if __name__ == '__main__':
    producer_demo()
