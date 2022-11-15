import random

import paho.mqtt.client as mqtt
import time


class Mqtt:

    def __init__(self):
        self.device = mqtt.Client()
        self.device.on_connect = self.on_connect
        self.device.on_message = self.on_message
        self.device.on_publish = self.on_publish
        self.device.on_disconnect = self.on_disconnect
        self.device.on_unsubscribe = self.on_unsubscribe
        self.device.on_subscribe = self.on_subscribe
        self.topic = None
        self.payload = None

    def publish_kafka(self, kafka_server, key):
        while True:

            if self.topic is not None and self.payload is not None:
                topic_key = self.topic.split("/")
                # print("Kafka pulish topic:" + self.topic + ", msg:" + self.payload.decode("utf-8"))
                # kafka_server.send(self.topic, key, self.payload.decode("utf-8"))
                # time.sleep(2)
                print("Kafka pulish topic:" + topic_key[1] + ", key:"+topic_key[0]+", msg:" + self.payload.decode("utf-8"))
                kafka_server.send(topic_key[1], topic_key[0], self.payload.decode("utf-8"))
                time.sleep(2)

    # def printTest(self):
    #     while True:
    #         # print("test")
    #         print(self.topic)
    #         print(self.payload)
    #         time.sleep(2)

    def connect_mqtt(self, url, port):
        self.device.connect(url, port)

    def publish_mqtt(self, topic, msg, qos, retain):

        self.device.publish(topic=topic, payload=msg, qos=qos, retain=retain)

    def subscribe_mqtt(self, topic, qos):
        self.device.subscribe(topic=topic, qos=qos)
        self.device.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))

    def on_message(self, client, userdata, msg):
        self.topic = msg.topic
        self.payload = msg.payload
        # print(msg.topic + " " + str(msg.payload))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)
        pass

    def on_unsubscribe(self, client, userdata, mid, granted_qos):
        print("On unSubscribed: qos = %d" % granted_qos)
        pass

    def on_publish(self, client, userdata, mid):
        # print("On onPublish: id = %d" % mid)
        time.sleep(2)
        pass

    def on_disconnect(self, client, userdata, rc):
        print("Unexpected disconnection rc = " + str(rc))
        pass

    def publish_mqtt_simulate(self, elevator):
        while True:

            if elevator == 1:
                self.device.publish(topic='elevator_001/destination-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/current-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/door', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_001/people', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_001/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator_001/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator_001/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_001/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator_001/alarm', payload='0', qos=1, retain=False)
                time.sleep(5)

            elif elevator == 2:
                self.device.publish(topic='elevator_002/destination-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/current-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/door', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_002/people', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_002/speed', payload=random.normalvariate(1.8, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator_002/spirit-level', payload=random.randrange(-9, 2), qos=0, retain=False)
                self.device.publish(topic='elevator_002/weight', payload=random.normalvariate(900, 300), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/hight-difference', payload=random.randrange(-1, 18), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/vibration-amplitude', payload=random.randrange(10), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/vibration-period', payload=random.randrange(-10, 10), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_002/voltage', payload=random.normalvariate(1, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator_002/alarm', payload='0', qos=1, retain=False)
                time.sleep(5)

            elif elevator == 3:
                self.device.publish(topic='elevator_003/destination-floor', payload=random.randrange(-1, 4), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/current-floor', payload=random.randrange(-1, 4), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/door', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_003/people', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_003/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator_003/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator_003/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_003/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator_003/alarm', payload='0', qos=1, retain=False)
                time.sleep(5)
            elif elevator == 4:
                self.device.publish(topic='elevator_004/destination-floor', payload=random.randrange(-1, 3), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/current-floor', payload=random.randrange(-1, 3), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/door', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_004/people', payload=random.randrange(0, 1), qos=0, retain=False)
                self.device.publish(topic='elevator_004/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator_004/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator_004/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator_004/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator_004/alarm', payload='0', qos=1, retain=False)
                time.sleep(5)
