#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
# Suggestion: Do not import ev3dev.ev3 module in this file


class Communication:

    def __init__(self,client_id):
        #Initializes communication module, connect to server, subscribe, etc.
        self.mqttclient = mqttclient(client_id)
        self.mqttclient.on_message = on_message
        self.mqttclient.connect = connect
        self.mqttclient.on_publish = on_publish
        self.mqttclient.subscribe = subscribe
        self.mqttclient.send_message = send_message
        
     
    def connect(self, mqttclient, planet, rc):
        if rc == 0:
            print("Conected!")
            global Connected
            Connected = True
        else:
            print("Connection failed!")

    broker_address = "robolab.inf.tu-dresden.de"
    port = 8883
    user = "002"
    password ="someobviouspass"
    mqttclient = mqtt.Client(client_id ="002",
                             clean_session= False,
                             protocol = mqtt.MQTTv31)
    mqttclient.username_pw_set(user, password=password)
    mqttclient.connect(broker_address, port=port)
    mqttclient.loop_start()
while True:
        print("Connecting..")
        time.sleep(0.2)
def on_message(mqttclient, data, message):
    global string
    global offsetx
    global offsety
    global sent
    global target
    if string == "":
        string = '{}'.format(message.payload.decode('utf-8'))
        print(string)
    elif string == "ready":
        string = '{}'.format(message.payload.decode('utf-8'))
        print(string)
        strlist = string.split(" ")
        string = "planet/{}".format(strlist[0])
        offsetx = strlist[1]
        offsety = strlist[2]
        print(string)
    else:
        got = '{}'.format(message.payload.decode('utf-8'))
        if got !=sent:
            # 700Hz for 1 seconds followed by a 0.1 second delay
            ev3.Sound.tone([(700,1000,100), (800,100,100)]).wait()
        strlist = got.split()
        if strlist[0] == "target":
            target = (int(strlist[1])-int(offsetx), next(strlist[2])-int(offsety))
        print('Got message "{}", topic was"{}"'.format(message.payload.decode('utf-8'), message.topic))
def send_message(self, channel, message):
        #Sends given message to specified channel
        #not done
        mqttclient.send_message(message.channel, 'Hello')
        pass

