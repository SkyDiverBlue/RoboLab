#left hand line follower
#Pid controller

import ev3dev.ev3 as ev3
import time

ev3.Sound.speak('line following has been initialised').wait()

class LineFollowing:
    def __init__(self, colour_sensor, motor_list, ts_list):
        self.left_motor, self.right_motor = motor_list
        
        self.colour_sensor = colour_sensor
        self.colour_sensor.mode = 'RGB-RAW' #Colour sensor is in Raw mode

        self.left_touch_sensor, self.right_touch_sensor = ts_list

        self.white_luminance_value = 0
        self.black_luminance_value = 0

        self.offset = 0


    def colour_calibration(self): #in this function both luminance will be calibrated 
        self.black_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        self.motor_left.run_timed(time_sp=500, speed_sp=200) 
        duty_cycled(20)
        self.motor_right.run_timed(time_sp=500, speed_sp=200) 
        duty_cycled(-20)
    # Startpositionen finden, später genauer definieren !!!
        self.white_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        self.motor_left.run_timed(time_sp=500, speed_sp=200) 
        duty_cycled(-20)
        self.motor_right.run_timed(time_sp=500, speed_sp=200) 
        duty_cycled(20)
        self.offset = (self.white_luminance_value + self.black_luminance_value) / 2


    def line_following(self):
        actual_luminance = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        last_error=0

        derivative=0
        integral=0

        Kp = 1 #Constant for the proportional controller (increase -> sharper turns, decrease -> smoother turns)
        Ki = 1 #Contant with intergral (summ of running errors)
        Kd = 1 #Constant with derivative (rate of change of the proportional value)

        error = actual_luminance - offset
        integral = integral + error
        derivative = error - last_error
        error = last_error

        turn = (Kp*error)+(Ki*integral)+(Kd*derivative)  
    
        
        if self.left_touch_sensor.value(self) ==1 or self.right_touch_sensor.value() == 1:
            ev3.Sound.speak('obstacle encountered')
            self.left_motor.stop()
            self.right_motor.stop() 
    
        self.colour_calibration()
        self.line_following()
