import json

from kafka import KafkaConsumer


class ConsumerKafka:
    def __init__(self, bootstrap_servers, topic):
        self.consumer = KafkaConsumer(
            topic,
            security_protocol="PLAINTEXT",
            bootstrap_servers=bootstrap_servers
        )
        # self.consumer.subscribe(pattern='mqtt11.*')

    def print_msg(self):
        for message in self.consumer:
            print("receive, topic: {} key: {}, value: {}".format(
                message.topic,
                json.loads(message.key.decode()),
                json.loads(message.value.decode())))
# def consumer_demo():
#     consumer = KafkaConsumer(
#         'topic',
#         security_protocol="PLAINTEXT",
#         bootstrap_servers=[
#             'localhost:9093',
#             'localhost:9094',
#             'localhost:9095'
#         ],
#     )
#     for message in consumer:
#         print("receive, key: {}, value: {}".format(
#             json.loads(message.key.decode()),
#             json.loads(message.value.decode()
#         )
#         )
#
#
if __name__ == '__main__':
    consumerTest = ConsumerKafka(['localhost:9093',
                                  'localhost:9094',
                                  'localhost:9095'], "alarm")
    consumerTest.print_msg()
