# from mqtt_to_kafka import MqttToKafka
import threading

from mqtt import Mqtt
from producer_kafka import ProducerKafka

if __name__ == '__main__':
    mqtt_subscribe1 = Mqtt()
    mqtt_subscribe1.connect_mqtt('localhost', 1883)

    producer_kafka1 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread1 = threading.Thread(target=mqtt_subscribe1.publish_kafka, args=[producer_kafka1, 'key1'])
    thread1.start()
    # 可能需要thread
    mqtt_subscribe1.subscribe_mqtt('elevator_001/#', qos=0)
    # mqtt_subscribe1.subscribe_mqtt('elevator_002/#', qos=0)





    mqtt_subscribe2 = Mqtt()
    mqtt_subscribe2.connect_mqtt('localhost', 1884)

    producer_kafka2 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread1 = threading.Thread(target=mqtt_subscribe2.publish_kafka, args=[producer_kafka2, 'key2'])
    thread1.start()

    mqtt_subscribe2.subscribe_mqtt('elevator_003/#', qos=0)






    mqtt_subscribe3 = Mqtt()
    mqtt_subscribe3.connect_mqtt('localhost', 1885)

    producer_kafka3 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread1 = threading.Thread(target=mqtt_subscribe3.publish_kafka, args=[producer_kafka3, 'key3'])
    thread1.start()

    mqtt_subscribe3.subscribe_mqtt('elevator_004/#', qos=0)