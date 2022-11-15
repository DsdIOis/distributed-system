import threading

from mqtt import Mqtt

if __name__ == '__main__':
    mqtt_simulate3 = Mqtt()
    mqtt_simulate3.connect_mqtt('localhost', 1885)
    mqtt_simulate3.publish_mqtt_simulate(4)
