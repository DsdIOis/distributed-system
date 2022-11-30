# from mqtt_to_kafka import MqttToKafka
import threading

from mqtt import Mqtt
from producer_kafka import ProducerKafka

if __name__ == '__main__':
    






    mqtt_subscribe3 = Mqtt()
    mqtt_subscribe3.connect_mqtt('localhost', 1885)

    producer_kafka3 = ProducerKafka(['localhost:9093',
                                     'localhost:9094',
                                     'localhost:9095'])

    threading.Thread()
    thread1 = threading.Thread(target=mqtt_subscribe3.publish_kafka, args=[producer_kafka3, 'key3'])
    thread1.start()

    mqtt_subscribe3.subscribe_mqtt('elevator/004/#', qos=0)