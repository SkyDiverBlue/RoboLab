# Suggestion: 	implement odometry as class that is not using the ev3dev.ev3 package
# 				establish value exchange with main driving class via getters and setters

import math


class Odometry:
    def __init__(self, motor_list):
        self.heading = 0 #north value
        self.grid_value = 30
        self.wheel_separation = 6
        self.wheel_circumference = 17.27
        self.left_motor, self.right_motor = motor_list

    def wheel_movement(self):

