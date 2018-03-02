#!/usr/bin/env python3

import paho.mqtt.client as mqtt
# Suggestion: Do not import ev3dev.ev3 module in this file


class Communication:

    def __init__(self, planet, mqtt_client):
        """ Initializes communication module, connect to server, subscribe, etc. """
        self.client = mqtt_client
        self.client.on_message = self.on_message

    def on_message(self, client, data, message):
        """ Handles the callback if any message arrived """
        pass

    def send_message(self, channel, message):
        """ Sends given message to specified channel """
        pass
