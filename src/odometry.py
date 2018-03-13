# Suggestion: 	implement odometry as class that is not using the ev3dev.ev3 package
# 				establish value exchange with main driving class via getters and setters

from math import *

class Odometry:
    def __init__(self):
        #do not set heading or rotatation to zero
        self.heading = (pi/180)*(5) #north value
        
        #self.wheel_separation = 11 #to be determined
        self.encoder_scale_factor = 5.5*pi / 360 #0.04363323129985823942309226921222
        self.wheel_separation = 11.5
        
        displacement = 0
        
        self.last_left = None
        self.last_right = None
        
        self.position_x = 0 
        self.position_y = 0

        self.coordinates_dic = {'x coordinate' : self.coordinates_x, 'y coordinate' : self.coordinates_y, 'direction' : self.compass}
        


    @property
    def coordinate_dic(self):
        return {'x coordinate' : self.coordinates_x, 'y coordinate' : self.coordinates_y, 'direction' : self.compass}

    def reset(self):
        self.last_left = None
        self.last_right = None

    
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
        
        self.position_y = self.position_y + displacement * cos(self.heading + rotation/2)
        self.position_x = self.position_x + displacement * sin(self.heading + rotation/2)
        self.heading = self.heading + rotation
        self.last_left = left
        self.last_right = right
        self.heading_degrees = self.heading * (180 / pi)

    @property
    def coordinates_y(self):
        return round(self.position_y/50)

    @coordinates_y.setter
    def coordinates_y(self, value):
        self.position_y = value * 50

        
    @property
    def coordinates_x(self):
        return round(self.position_x/50)

    @coordinates_x.setter
    def coordinates_x(self, value):
        self.position_x = value * 50

    @property
    def compass(self):
        modulo_calculation = self.heading_degrees % 360
        
        if modulo_calculation > 45 and modulo_calculation <= 135:
            return 'E'

        elif modulo_calculation >= 315 or modulo_calculation <= 45:
            return 'N'
        
        elif modulo_calculation > 135 and modulo_calculation <= 225:
            return  'S'
        else: 
            return 'W'
        





        
        
        





