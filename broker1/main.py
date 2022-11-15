import paho.mqtt.client as mqtt
import time
import random


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
    device.connect('localhost', 1883)

    while True:

        device.publish(topic='elevator_001/destination-floor', payload=random.randrange(-1,8), qos=0, retain=False)
        device.publish(topic='elevator_001/current-floor', payload=random.randrange(-1,8), qos=0, retain=False)
        device.publish(topic='elevator_001/door', payload=random.randrange(0,1), qos=0, retain=False)
        device.publish(topic='elevator_001/people', payload=random.randrange(0,1), qos=0, retain=False)
        device.publish(topic='elevator_001/speed', payload=random.normalvariate(2,0.3), qos=0, retain=False)
        device.publish(topic='elevator_001/spirit-level', payload=random.randrange(-5,5), qos=0, retain=False)
        device.publish(topic='elevator_001/weight', payload=random.normalvariate(500,100), qos=0, retain=False)
        device.publish(topic='elevator_001/hight-difference', payload=random.randrange(-10,8), qos=0, retain=False)
        device.publish(topic='elevator_001/vibration-amplitude', payload=random.randrange(0,8), qos=0, retain=False)
        device.publish(topic='elevator_001/vibration-period', payload=random.randrange(-10,8), qos=0, retain=False)
        device.publish(topic='elevator_001/voltage', payload=random.normalvariate(0,0.1), qos=0, retain=False)
        device.publish(topic='elevator_001/alarm', payload='0', qos=1, retain=False)

        device.publish(topic='elevator_002/destination-floor', payload=random.randrange(-1,8), qos=0, retain=False)
        device.publish(topic='elevator_002/current-floor', payload=random.randrange(-1,8), qos=0, retain=False)
        device.publish(topic='elevator_002/door', payload=random.randrange(0,1), qos=0, retain=False)
        device.publish(topic='elevator_002/people', payload=random.randrange(0,1), qos=0, retain=False)
        device.publish(topic='elevator_002/speed', payload=random.normalvariate(1.8,0.3), qos=0, retain=False)
        device.publish(topic='elevator_002/spirit-level', payload=random.randrange(-9,2), qos=0, retain=False)
        device.publish(topic='elevator_002/weight', payload=random.normalvariate(900,300), qos=0, retain=False)
        device.publish(topic='elevator_002/hight-difference', payload=random.randrange(-1,18), qos=0, retain=False)
        device.publish(topic='elevator_002/vibration-amplitude', payload=random.randrange(10), qos=0, retain=False)
        device.publish(topic='elevator_002/vibration-period', payload=random.randrange(-10,10), qos=0, retain=False)
        device.publish(topic='elevator_002/voltage', payload=random.normalvariate(1,0.1), qos=0, retain=False)
        device.publish(topic='elevator_002/alarm', payload='0', qos=1, retain=False)

        time.sleep(2)
