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
        self.payload=[[], [], [], [], [],[],[],[],[],[],[],[]]
        self.key=None
        self.topics=['destination-floor','current-floor','door','people','speed','spirit-level','weight','hight-difference','vibration-amplitude','vibration-period','voltage','alarm']
        self.enablesend=0;
    def publish_kafka(self, kafka_server, key):
        while True:
            time.sleep(0.01)
            
            if self.enablesend>9 :
                self.enablesend=0
            
            
                print('start')
                for i in range(len(self.payload)):
                    print(self.topics[i]+str(self.payload[i]))
                    
                        
                    result=0
                    for x in self.payload[i]:
                        result+=x
                    result/=len(self.payload[i])
                    if(self.topics[i]=='alarm' or self.topics[i]=='people'):
                        if(result>0):
                            result=1
                        else:
                            result=0
                    print("Kafka pulish topic:" + self.topics[i] + ", key:"+self.key+", msg:" + str(result))
                    kafka_server.send(self.topics[i], self.key, str(result))
                
                self.payload=[[], [], [], [], [],[],[],[],[],[],[],[]]
            
#           time.sleep(1)
#            for i in range(len(self.payload)):
#                result=0
                
#                for j in range(len(self.payload[i])):
#                    result=result+self.payload[i][j]
#                    print(self.payload[i].decode("utf-8"))
#                result=result/len(self.payload[i])
#                
#            self.payload=payload=[[0]*12]*10
            
            


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
        
        topic_key = msg.topic.split("/")
        if(topic_key[2]=='enablesend' and str(msg.payload.decode("utf-8"))=='enable' ):
            
            self.enablesend+=1
            print(self.enablesend)
            
        # print(topic_key[2])
        #print(float(str(msg.payload.decode("utf-8"))))
        #print(self.topics.index(topic_key[2]))

        else:
            self.payload[self.topics.index(topic_key[2])].append(float(str(msg.payload.decode("utf-8"))))

            self.key=topic_key[1]
        
        
        # print(msg.topic + " " + str(msg.payload))
            
        

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)
        pass

    def on_unsubscribe(self, client, userdata, mid, granted_qos):
        print("On unSubscribed: qos = %d" % granted_qos)
        pass

    def on_publish(self, client, userdata, mid):
        # print("On onPublish: id = %d" % mid)
        time.sleep(0.1)

        pass

    def on_disconnect(self, client, userdata, rc):
        print("Unexpected disconnection rc = " + str(rc))
        pass

    def publish_mqtt_simulate(self, elevator):
        while True:
            
            if elevator == 1:
                self.device.publish(topic='elevator/001/destination-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/current-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/door', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/001/people', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/001/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator/001/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator/001/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/001/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator/001/alarm', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/001/enablesend', payload='enable', qos=0, retain=False)

            elif elevator == 2:
                self.device.publish(topic='elevator/002/destination-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/current-floor', payload=random.randrange(-1, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/door', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/002/people', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/002/speed', payload=random.normalvariate(1.8, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator/002/spirit-level', payload=random.randrange(-9, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/002/weight', payload=random.normalvariate(900, 300), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/hight-difference', payload=random.randrange(-1, 18), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/vibration-amplitude', payload=random.randrange(10), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/vibration-period', payload=random.randrange(-10, 10), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/002/voltage', payload=random.normalvariate(1, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator/002/alarm', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/002/enablesend', payload='enable', qos=0, retain=False)

            elif elevator == 3:
                self.device.publish(topic='elevator/003/destination-floor', payload=random.randrange(-1, 4), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/current-floor', payload=random.randrange(-1, 4), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/door', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/003/people', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/003/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator/003/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator/003/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/003/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator/003/alarm', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/003/enablesend', payload='enable', qos=0, retain=False)
            elif elevator == 4:
                self.device.publish(topic='elevator/004/destination-floor', payload=random.randrange(-1, 3), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/current-floor', payload=random.randrange(-1, 3), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/door', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/004/people', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/004/speed', payload=random.normalvariate(2, 0.3), qos=0, retain=False)
                self.device.publish(topic='elevator/004/spirit-level', payload=random.randrange(-5, 5), qos=0, retain=False)
                self.device.publish(topic='elevator/004/weight', payload=random.normalvariate(500, 100), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/hight-difference', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/vibration-amplitude', payload=random.randrange(0, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/vibration-period', payload=random.randrange(-10, 8), qos=0,
                                    retain=False)
                self.device.publish(topic='elevator/004/voltage', payload=random.normalvariate(0, 0.1), qos=0, retain=False)
                self.device.publish(topic='elevator/004/alarm', payload=random.randrange(0, 2), qos=0, retain=False)
                self.device.publish(topic='elevator/004/enablesend', payload='enable', qos=0, retain=False)
            #time.sleep(1)