# Suggestion: 	implement odometry as class that is not using the ev3dev.ev3 package
# 				establish value exchange with main driving class via getters and setters

import math


class Odometry:
    def __init__(self):
        #do not set heading or rotatation to zero
        #self.heading = 0 #north value
        
        self.wheel_separation = 4.5 #to be determined
        self.encoder_scale_factor = 0.045378560551853

        self.displacement = 0
        
        self.right_rmp = 0 # right turn right motor position
        self.right_lmp = 0 # right turn left motor position
        
        self.left_rmp = 0 # left turn right motor position
        self.left_lmp = 0 # left turn right motor position

        self.sensor_wheels = 0 #to be determined -> distance between wheels and colour sensor

        self.position_x = 0
        self.position_y = 0
    
    def odometry_calculations(self):
        self.displacement = (self.left_rmp + self.right_lmp) * self.encoder_scale_factor / 2
        
        #self.rotation = ((self.left_lmp + self.right_rmp) * self.encoder_scale_factor) / self.wheel_separation

        #self.position_x = self.position_x + cos(self.heading + self.rotation) / 2
        #self.position_y = self.position_y + sin(self.heading + self.rotation) / 2
        #self.heading = self.heading + self.rotation
        
        





