#left hand line follower
#Pid controller

import ev3dev.ev3 as ev3
import time

ev3.Sound.speak('line following has been initialised')

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
        ev3.Sound.speak('in colour calibration').wait()
        self.black_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        
        print('{},{},{}'.format(self.colour_sensor.red, self.colour_sensor.green, self.colour_sensor.blue))
        
        self.left_motor.run_timed(time_sp=300, speed_sp=-100) 
        self.right_motor.run_timed(time_sp=300, speed_sp=100) 
        
        time.sleep(1)

    # Startpositionen finden, später genauer definieren !!!
        self.white_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        
        print('{},{},{}'.format(self.colour_sensor.red, self.colour_sensor.green, self.colour_sensor.blue))

        self.offset = (self.white_luminance_value + self.black_luminance_value) / 2  
        
        self.left_motor.run_timed(time_sp=100, speed_sp=200) 
        self.right_motor.run_timed(time_sp=100, speed_sp=-200)
        
        if 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue == self.offset:

            self.left_motor.stop()
            self.right_motor.stop()
        
        time.sleep (1)


        
       

    def line_following(self):
        actual_luminance = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        last_error=0

        derivative=0
        integral=0

        Kp = 1 #Constant for the proportional controller (increase -> sharper turns, decrease -> smoother turns)
        Ki = 1 #Contant with intergral (summ of running errors)
        Kd = 1 #Constant with derivative (rate of change of the proportional value)

        error = actual_luminance - self.offset
        integral = integral + error
        derivative = error - last_error
        error = last_error

        turn = (Kp*error)+(Ki*integral)+(Kd*derivative)  
        
        
        if self.left_touch_sensor.value() ==1 or self.right_touch_sensor.value() == 1:
            ev3.Sound.speak('obstacle encountered')
            self.left_motor.stop()
            self.right_motor.stop() 
