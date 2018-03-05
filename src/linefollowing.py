#left hand line follower
#Pid controller

import ev3dev.ev3 as ev3
import time

ev3.Sound.speak('line following has been initialised').wait()

class LineFollowing:
    def __init__(self):
        self.left_motor = ev3.LargeMotor('outB')
        self.right_motor = ev3.LargeMotor('outC')
        
        self.colour_sensor = ev3.ColorSensor('in2')
        self.colour_sensor.mode = 'RGB-RAW' #Colour sensor is in Raw mode

        self.left_touch_sensor = ev3.TouchSensor('in1')
        self.right_touch_sensor = ev3.TouchSensor('in4')
        return

def colour_calibration(): #function to finde the target light value from the colour sensor
    black = 1



def line_following(self):
    target_light_value = target #the light target value witht the white and black from the line
    actual_light_value = value #actual light value read by the sensor

    Kp = 1 #Constant for the proportional controller (increase -> sharper turns, decrease -> smoother turns)
    Ki = 1 #Contant with intergral (summ of running errors)
    Kd = 1 #Constant with derivative (rate of change of the proportional value)
    error = 0 #
    integral = 0

    integral = integral + error
    derivative = error - last_error
    last_error = error

    turn = (target -  value) * Kp

    motor_speed = Kp * error + Kd * (error - last_error)


    
    
        
    if left_touch_sensor.value() ==1 or right_touch_sensor.value() == 1:
            ev3.Sound.speak('obstacle encountered')
            self.left_motor.stop()
            self.right_motor.stop() 
    

line_following(self)