#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from planet import Direction, Planet
from communication import Communication

import linefollowing as follow #imports the line following program as follow



def run():
# the execution of all code shall be started from within this function
    print('Hello World')
    follow #executes the line program


if __name__ == '__main__':
    run()