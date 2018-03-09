#!/usr/bin/env python3
import paho.mqtt.client as mqtt
# Suggestion: Do not import ev3dev.ev3 module in this file


class Communication:

    def __init__(self, planet):
        self.client = mqtt.Client(client_id="02", clean_session=False, protocol=mqtt.MQTTv31)
        self.planet = planet
        self.client.on_message = self.on_message
     
    def connect(self):
        self.client.username_pw_set(username="002", password="Gq5FnDuKW1") 
        self.client.connect('robolab.inf.tu-dresden.de', 8883)
        self.client.subscribe('explorer/002', qos=1) 
        self.client.loop_start()

    def on_message(self, client, data, message):
        print("Server message: " + str(message.topic) + "  " + str(message.payload.decode('utf-8')))
 
        pass
        
    

    def send_message(self, channel, message):
        
        print('test')
       
        pass


