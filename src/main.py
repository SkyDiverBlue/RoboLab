#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from planet import Direction, Planet
from odometry import Odometry
import linefollowing as follow #imports the line following program as follow
from movement import Movement



def run():
# the execution of all code shall be started from within this function
    print('Hello World')
    
    odometry = Odometry()
    movement_functions = Movement(motor_list = (ev3.LargeMotor('outB'), ev3.LargeMotor('outC')), odometry = odometry)
    line_follower = follow.LineFollowing(colour_sensor = ev3.ColorSensor('in2'),
                         ts_list = (ev3.TouchSensor('in1'), ev3.TouchSensor('in4')), movement=movement_functions, odometry = odometry)
    line_follower.colour_calibration()
    while True:
        #odometry.odometry_calculations()
        line_follower.line_following()
        line_follower.path_recognising()
        line_follower.touch_sensor()

    



if __name__ == '__main__':
    run()
    