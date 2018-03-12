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

    def on_message(self, client, data, msg):
        print("Server message: " + str(msg.topic) + "  " + str(msg.payload.decode('utf-8')))

        if 'explorer' in msg.topic:
            args = str(msg.payload.decode("utf-8")).split(" ")
            planet = args[2]
            self.client.subscribe((planet),qos=1)
            planet.set_start_point(eval(args[3]))


        elif 'planet' in msg.topic:
            args = str(msg.payload.decode("utf-8")).split(" ")
            if 'path' in args[1]:
                start = args[2].split(",")
                target = args[3].split(",")
                weight = args[5]
                planet.add_path()
               

            elif 'target' in args[1]:
                #empfangen von Zielkoordinaten an Planet

        pass 
    

    def send_message(self, channel, message):
        self.client.publish(#topic channel, payload = message, qos=1)

        
        print('test')
       
        pass


