#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from planet import Direction, Planet
from communication import Communication

import linefollowing as follow #imports the line following program as follow



def run():
# the execution of all code shall be started from within this function
    print('Hello World')
    follow.LineFollowing(colour_sensor = ev3.ColorSensor('in2'),
                         motor_list = (ev3.LargeMotor('outB'), ev3.LargeMotor('outC')),
                         ts_list = (ev3.TouchSensor('in1'), ev3.TouchSensor('in4')))
    #executes the line program


if __name__ == '__main__':
    run()