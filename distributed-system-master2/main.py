import paho.mqtt.client as mqtt
import time


def on_connect(client,userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client,userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_subscribe(client,userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)
    pass


def on_unsubscribe(client,userdata, mid, granted_qos):
    print("On unSubscribed: qos = %d" % granted_qos)
    pass


def on_publish(client, userdata, mid):
    print("On onPublish: id = %d" % mid)
    pass


def on_disconnect(client,userdata, rc):
    print("Unexpected disconnection rc = " + str(rc))
    pass


if __name__ == '__main__':
    # we will simulate 3 devices SmartHome to publish their mensajes

    device = mqtt.Client()
    device.on_connect = on_connect
    device.on_message = on_message
    device.on_publish = on_publish
    device.on_disconnect = on_disconnect
    device.on_unsubscribe = on_unsubscribe
    device.on_subscribe = on_subscribe
    device.connect('localhost', 1884)

    while True:
        device.publish(topic='home2/device1', payload='On, 11:11:14', qos=0, retain=False)
        # time.sleep(2)
        device.publish(topic='home2/device2', payload='On, 5% Hum', qos=0, retain=False)
        # time.sleep(2)
        device.publish(topic='home2/device3', payload='Off', qos=0, retain=False)
        time.sleep(2)
