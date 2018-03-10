# Suggestion: 	implement odometry as class that is not using the ev3dev.ev3 package
# 				establish value exchange with main driving class via getters and setters

from math import *


class Odometry:
    def __init__(self):
        #do not set heading or rotatation to zero
        self.heading = 0 #north value
        
        self.wheel_separation = 10 #to be determined
        self.encoder_scale_factor = 0.04363323129985823942309226921222

        self.displacement = 0
        
        self.last_left = None
        self.last_right = None

        self.sensor_wheels = 0 #to be determined -> distance between wheels and colour sensor

        self.position_x = 0
        self.position_y = 0
    
    def odometry_calculations(self, left_motor, right_motor):
        
        left = left_motor.position 
        right = right_motor.position
        if self.last_left is None or self.last_right is None:
            self.last_left = left
            self.last_right = right
        
        delta_left = left - self.last_left
        delta_right = right - self.last_right
        
        displacement = (delta_left + delta_right) * self.encoder_scale_factor / 2
        
        rotation = ((delta_left - delta_right) * self.encoder_scale_factor) / self.wheel_separation
        
        self.position_y = self.position_x + displacement * cos(self.heading + rotation/2)
        self.position_x = self.position_y + displacement * sin(self.heading + rotation/2)
        self.heading = self.heading + rotation
        self.last_left = left
        self.last_right = right
        self.heading_degrees = self.heading * (180 / pi)



        
        
        





