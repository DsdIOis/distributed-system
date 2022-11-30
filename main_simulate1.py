import threading

from mqtt import Mqtt

if __name__ == '__main__':
    mqtt_simulate1 = Mqtt()
    mqtt_simulate1.connect_mqtt('localhost', 1883)
    mqtt_simulate1.publish_mqtt_simulate(1)
    mqtt_simulate1.publish_mqtt_simulate(2)
    
    # mqtt_simulate1.publish_mqtt_simulate(2)
    #
    # mqtt_simulate2 = Mqtt()
    # mqtt_simulate2.connect_mqtt('localhost', 1884)
    # mqtt_simulate2.publish_mqtt_simulate(3)
    #
    # mqtt_simulate3 = Mqtt()
    # mqtt_simulate3.connect_mqtt('localhost', 1885)
    # mqtt_simulate3.publish_mqtt_simulate(4)
