#right hand line follower
#Pid controller

import ev3dev.ev3 as ev3
import time

ev3.Sound.speak('line following has been initialised')

class LineFollowing:
    def __init__(self, colour_sensor, ts_list, movement):
                
        self.colour_sensor = colour_sensor
        self.colour_sensor.mode = 'RGB-RAW' #Colour sensor is in Raw mode

        self.left_touch_sensor, self.right_touch_sensor = ts_list

        self.movement = movement

        self.white_luminance_value = 0
        self.black_luminance_value = 0
        
        self.offset = 0

    def colour_calibration(self): #in this function both luminance (black/white) will be calibrated
        ev3.Sound.speak('in colour calibration').wait()
        
        self.black_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        print('{},{},{}'.format(self.colour_sensor.red, self.colour_sensor.green, self.colour_sensor.blue))
        
        #robot turns
                
        self.movement.turn_left_relpos(p = 400 , s = 200)

                       
        time.sleep(1)

        self.white_luminance_value = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
        print('{},{},{}'.format(self.colour_sensor.red, self.colour_sensor.green, self.colour_sensor.blue))

        self.offset = (self.white_luminance_value + self.black_luminance_value) / 2
        print(self.offset)
        
        #robot turns back

        self.movement.tright_run_timed(t = 1000,s = 80)
               
        #robot stops when it detects offset as luminance value
        if 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue == self.offset:

            self.movement.stop_run_timed()
        
        time.sleep(1)   
       

    def line_following(self):
        ev3.Sound.speak('calibration complete')

        speed_base = 125

        last_error = 0
        derivative = 0
        integral = 0
        

        Kp = 0.07 #Constant for the proportional controller (increase -> sharper turns, decrease -> smoother turns)
        Ki = 0.05 #Contant with intergral (summ of running errors)
        Kd = 0.8 #Constant with derivative (rate of change of the proportional value)
                
        #luminance value for offset = 201.1286
        #while luminance equal to calibrate luminance, the drive ahead. 
        #If luminance increases -> wobble right
        #If luminance decreases -> wobble left
        
        while True:
            actual_luminance = 0.2126*self.colour_sensor.red+0.7152*self.colour_sensor.green+0.0722*self.colour_sensor.blue
            error = actual_luminance - self.offset
            integral = integral + error
            derivative = error - last_error
            turn = (Kp*error)+(Ki*integral)+(Kd*derivative)

            if error > 0:
                
                self.movement.ttright_run_timed(t =100, s1 = speed_base - turn, s2 = speed_base + turn)
                error = last_error
                
            else:

                self.movement.ttleft_run_timed(t = 100, s1 = speed_base + turn, s2 = speed_base - turn)
                
            last_error = error
        
        if self.left_touch_sensor.value() ==1 or self.right_touch_sensor.value() == 1: 
            
            self.movement.stop_run_timed()
               
    def path_recognising(self):
        if self.colour_sensor.value == colour_sensor.red < 100 and colour_sensor.blue > 105 or self.colour_sensor.value == colour_sensor.red > 140 and colour_sensor.green < 100 and colour_sensor.blue < 50:
            print('colour')

        

