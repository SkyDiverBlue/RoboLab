#!/usr/bin/env python3
import paho.mqtt.client as mqtt
# Suggestion: Do not import ev3dev.ev3 module in this file
from odometry import Odometry
from planet import Planet
from linefollowing import Linefollowing


class Communication:

    def __init__(self, planet):
        self.client = mqtt.Client(client_id="02", clean_session=False, protocol=mqtt.MQTTv31)
        self.planet = planet
        self.client.on_message = self.on_message
        self.odometry = odometry
     
    def connect(self):
        self.client.username_pw_set(username="002", password="Gq5FnDuKW1") 
        self.client.connect('robolab.inf.tu-dresden.de', 8883)
        self.client.subscribe('explorer/002', qos=1) 
        self.client.loop_start()

    def on_message(self, client, data, msg):
        print("Server message: " + str(msg.topic) + "  " + str(msg.payload.decode('utf-8')))

        if 'explorer' in msg.topic:
            args = str(msg.payload.decode("utf-8")).split(" ")
            self.planet.name = args[2]
            self.client.subscribe((planet),qos=1)
            planet.set_start_point(eval(args[3]))


        elif 'planet' in msg.topic:
            args = str(msg.payload.decode("utf-8")).split(" ")
            if 'path' in args[1]:
                start = args[2].split(",")
                target = args[3].split(",")
                weight = args[5]
                planet.add_path(start, target, weight)
               

            elif 'target' in args[1]:
                #empfangen von Zielkoordinaten an Planet
                pass 
    

    def send_message(self, channel, message):
        self.client.publish(t = message.topic, b = message.payload, qos=1)
        pass


    def first_communication(self) :
        self.connect()
        self.send_message('explorer/002', 'SYN Ready')
        self.client.subscribe('planet/{}'.format(self.planet.name), qos=1)
        pass

    def path_communication(self) :
        if communication_on == True:
            if planet.start_dict=={}:
                start.odo =(self.planet.start_point, N)
            else :
                start_odo = (x,y ,heading)
                target_odo = (self.odometry.coordinates_x, self.coordinates_y, self.odometry.invertcompass_directions)
                self.send_message('planet/{}'.format(self.planet.name), 'SYN path', '{}'.format(start_odo), '{}'.format(target_odo), '{}'.format(self.linefollowing.status))