#!/usr/bin/env python3
import paho.mqtt.client as mqtt
# Suggestion: Do not import ev3dev.ev3 module in this file


class Communication:

    def __init__(self, planet, mqtt_client):
        #Initializes communication module, connect to server, subscribe, etc.
        self.client = mqtt_client
        self.planet = planet
        self.client.on_message = self.on_message
     
    def connect(client, host, port, username, password,subscribe):
        client = mqtt.Client(client_id="02",
                             clean_session=False,
                             protocol=mqtt.MQTTv31)
        client.connect = connect
        client.username_pw_set(username="002", password="someobviouspass") #Set a username and pass for broker authentication.
        client.connect('robolab.inf.tu-dresden.de', 8883)
        client.subscribe('explorer/002', qos=1) # subscribe to topic explorer/002
        client.loop_forever()
        while True:
            time.sleep(2)

    def on_message(client, data, message):
        print('Message received!')
        #print('content: ' + message.content + ', qos: ' + 
          #str(message.qos) + ', message: ' + str(message.payload))
        client.on_message = on_message
    

    def send_message(self, channel, message):
        #Sends given message to specified channel
        #not done
        print('test')
       
        pass


