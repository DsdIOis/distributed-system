# from mqtt_to_kafka import MqttToKafka
import threading

from mqtt import Mqtt
from producer_kafka import ProducerKafka

if __name__ == '__main__':
    




    mqtt_subscribe2 = Mqtt()
    mqtt_subscribe2.connect_mqtt('localhost', 1884)

    producer_kafka2 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread1 = threading.Thread(target=mqtt_subscribe2.publish_kafka, args=[producer_kafka2, 'key2'])
    thread1.start()

    mqtt_subscribe2.subscribe_mqtt('elevator/003/#', qos=0)



