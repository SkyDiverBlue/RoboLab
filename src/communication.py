#!/usr/bin/env python3
import paho.mqtt.client as mqtt
# Suggestion: Do not import ev3dev.ev3 module in this file
from planet import *
import string
from random import *
import time


class Communication:

    def __init__(self, planet, odometry):
        self.client = mqtt.Client(client_id=self.new_id(), clean_session=False, protocol=mqtt.MQTTv31)
        self.planet = planet
        self.client.on_message = self.on_message
        self.odometry = odometry
        self.planet_name = ''
    def new_id(self):
        min = 6
        max = 8
        newString = string.ascii_letters + string.punctuation + string.digits
        return "".join(choice(newString) for x in range(randint(min,max)))

     
    def connect(self):
        self.client.username_pw_set(username="002", password="Gq5FnDuKW1") 
        self.client.connect('robolab.inf.tu-dresden.de', 8883)
        self.client.subscribe('explorer/002', qos=1) 
        self.client.loop_start()

    def on_message(self, client, data, msg):
        if 'ACK' in msg.payload.decode('utf-8'):
            print("Server message: " + str(msg.topic) + "  " + str(msg.payload.decode('utf-8')))

            if 'explorer' in msg.topic :
                args = str(msg.payload.decode("utf-8")).split(" ")
                self.planet_name = args[1]
                start_pnt= list(args[2].split(","))
                start_pnt[0]=int(start_pnt[0])
                start_pnt[1]=int(start_pnt[1])
                start_pnt = tuple(start_pnt)
                self.planet.set_start_point((start_pnt))


            elif 'planet' in msg.topic:
                args = str(msg.payload.decode("utf-8")).split(" ")
                if 'path' in args[1]:
                    start = list(args[2].split(","))
                    target = list(args[3].split(","))
                    start[0]=int(start[0])
                    start[1] = int(start[1])
                    start[2] = self.planet.communication_direction_converter(start[2]) 
                    target [0] = int(target[0])
                    target [1] = int(target[1])
                    target [2] = self.planet.communication_direction_converter(target[2])  
                    start = tuple(start)
                    target=tuple(target)
                    weight = int(args[5])
                    planet.add_path(start, target, weight)
               

            elif 'target' in args[1]:
                #empfangen von Zielkoordinaten an Planet
                pass 
    

    def send_message(self, channel, message):
        self.client.publish(channel, payload=message, qos=1)
        pass


    def first_communication(self) :
        time.sleep(3)
        self.send_message('explorer/002', 'SYN ready')
        time.sleep(3)
        self.client.subscribe('planet/{}'.format(self.planet_name), qos=1)
        pass

    def path_communication(self) :
        if communication_on == True:
            if planet.start_dict=={}:
                start.odo =(self.planet.start_point, N)
            else :
                start_odo = (x,y ,heading)
                target_odo = (self.odometry.coordinates_x, self.coordinates_y, self.odometry.invertcompass_directions)
                self.send_message('planet/{}'.format(self.planet_name), 'SYN path', '{}'.format(start_odo), '{}'.format(target_odo), 'status')





