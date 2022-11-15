import threading

from mqtt import Mqtt


def publish_thread(mqtt_simulate, index):
    mqtt_simulate.publish_mqtt_simulate(index)


if __name__ == '__main__':
    mqtt_simulate1 = Mqtt()
    mqtt_simulate1.connect_mqtt('localhost', 1883)

    mqtt_simulate2 = Mqtt()
    mqtt_simulate2.connect_mqtt('localhost', 1883)

    mqtt_simulate3 = Mqtt()
    mqtt_simulate3.connect_mqtt('localhost', 1884)

    mqtt_simulate4 = Mqtt()
    mqtt_simulate4.connect_mqtt('localhost', 1885)

    threading.Thread()
    thread1 = threading.Thread(target=publish_thread, args=[mqtt_simulate1, 1])
    thread2 = threading.Thread(target=publish_thread, args=[mqtt_simulate2, 2])
    thread1.start()
    thread2.start()
   
    thread3 = threading.Thread(target=publish_thread, args=[mqtt_simulate3, 3])
    thread4 = threading.Thread(target=publish_thread, args=[mqtt_simulate4, 4])
    thread3.start()
    thread4.start()
    # mqtt_simulate1 = Mqtt()
    # mqtt_simulate1.connect_mqtt('localhost', 1883)
    # mqtt_simulate1.publish_mqtt_simulate(1)

    #
    # mqtt_simulate2 = Mqtt()
    # mqtt_simulate2.connect_mqtt('localhost', 1884)
    # mqtt_simulate2.publish_mqtt_simulate(3)
    #
    # mqtt_simulate3 = Mqtt()
    # mqtt_simulate3.connect_mqtt('localhost', 1885)
    # mqtt_simulate3.publish_mqtt_simulate(4)
