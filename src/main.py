#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from planet import Direction, Planet
from communication import Communication

def run():
    # the execution of all code shall be started from within this function
    print("Hello Marine")ev3.Sound.speak('Welcome to our Robolab project!').wait() #makes robot speakdef run():	#motor right + left	motorleft = ev3.LargeMotor('outB')
	motorright=ev3.LargeMotor('outC')

	motorleft.run_timed(time_sp=3000, speed_sp=500)	motorright.run_timed(time_sp=3000, speed_sp=500)




if __name__ == '__main__':
    run()
