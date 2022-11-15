# from mqtt_to_kafka import MqttToKafka
import threading

from mqtt import Mqtt
from producer_kafka import ProducerKafka


def thread_subscribe(mqtt_subscribe, topic, producer_kafka,thread_sub):
    # mqtt_subscribe = Mqtt()
    # mqtt_subscribe.connect_mqtt('localhost', 1883)
    #
    # producer_kafka = ProducerKafka(['localhost:9093',
    #                                   'localhost:9094',
    #                                   'localhost:9095'])

    threading.Thread()
    thread_sub = threading.Thread(target=mqtt_subscribe.publish_kafka, args=[producer_kafka, 'key'])
    thread_sub.start()
    mqtt_subscribe.subscribe_mqtt(topic, qos=0)


if __name__ == '__main__':
    mqtt_subscribe1 = Mqtt()
    mqtt_subscribe1.connect_mqtt('localhost', 1883)

    producer_kafka1 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    mqtt_subscribe2 = Mqtt()
    mqtt_subscribe2.connect_mqtt('localhost', 1883)

    producer_kafka2 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    mqtt_subscribe3 = Mqtt()
    mqtt_subscribe3.connect_mqtt('localhost', 1884)

    producer_kafka3 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    mqtt_subscribe4 = Mqtt()
    mqtt_subscribe4.connect_mqtt('localhost', 1885)

    producer_kafka4 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread_sub1 = None
    thread1 = threading.Thread(target=thread_subscribe,
                               args=[mqtt_subscribe1, 'elevator_001/#', producer_kafka1, thread_sub1])
    thread1.start()

    thread_sub2 = None
    thread2 = threading.Thread(target=thread_subscribe,
                               args=[mqtt_subscribe2, 'elevator_002/#', producer_kafka2, thread_sub2])
    thread2.start()

    thread_sub3 = None
    thread3 = threading.Thread(target=thread_subscribe,
                               args=[mqtt_subscribe3, 'elevator_003/#', producer_kafka3, thread_sub3])
    thread3.start()

    thread_sub4 = None
    thread4 = threading.Thread(target=thread_subscribe,
                               args=[mqtt_subscribe4, 'elevator_004/#', producer_kafka4, thread_sub4])
    thread4.start()

    # threading.Thread()
    # thread12 = threading.Thread(target=thread_subscribe)
    # thread12.start()
    #
    # mqtt_subscribe1 = Mqtt()
    # mqtt_subscribe1.connect_mqtt('localhost', 1883)
    #
    # producer_kafka1 = ProducerKafka(['localhost:9093',
    #                                  'localhost:9094',
    #                                  'localhost:9095'])
    #
    # threading.Thread()
    # thread1 = threading.Thread(target=mqtt_subscribe1.publish_kafka, args=[producer_kafka1, 'key1'])
    # thread1.start()
    # # 可能需要thread
    # mqtt_subscribe1.subscribe_mqtt('elevator_001/#', qos=0)

    # mqtt_subscribe1.subscribe_mqtt('elevator_002/#', qos=0)

    # mqtt_subscribe2 = Mqtt()
    # mqtt_subscribe2.connect_mqtt('localhost', 1884)
    #
    # producer_kafka2 = ProducerKafka(['localhost:9093',
    #                                  'localhost:9094',
    #                                  'localhost:9095'])
    #
    # threading.Thread()
    # thread1 = threading.Thread(target=mqtt_subscribe2.publish_kafka, args=[producer_kafka2, 'key2'])
    # thread1.start()
    #
    # mqtt_subscribe2.subscribe_mqtt('elevator_003/#', qos=0)
    #
    #
    #
    #
    #
    #
    # mqtt_subscribe3 = Mqtt()
    # mqtt_subscribe3.connect_mqtt('localhost', 1885)
    #
    # producer_kafka3 = ProducerKafka(['localhost:9093',
    #                                  'localhost:9094',
    #                                  'localhost:9095'])
    #
    # threading.Thread()
    # thread1 = threading.Thread(target=mqtt_subscribe3.publish_kafka, args=[producer_kafka3, 'key3'])
    # thread1.start()
    #
    # mqtt_subscribe3.subscribe_mqtt('elevator_004/#', qos=0)
