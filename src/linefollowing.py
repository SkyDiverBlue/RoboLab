#Line following program

import ev3dev.ev3 as ev3

def line_following():
    ev3.Sound.speak('line following has been initialised').wait()
    
    left_motor = ev3.LargeMotor('outB')
    right_motor = ev3.LargeMotor('outC')
    
    colour_sensor = ev3.ColorSensor('in2')
    colour_sensor.mode = 'COL-COLOR'

    left_touch_sensor = ev3.TouchSensor('in1')
    right_touch_sensor = ev3.TouchSensor('in4')
   
    while colour_sensor.value() == 1:
        left_motor.run_forever(speed_sp=500)
        right_motor.run_forever(speed_sp=500)                
        
        if left_touch_sensor.value() ==1 or right_touch_sensor.value() == 1:
            ev3.Sound.speak('obstacle encountered')
            left_motor.stop()
            right_motor.stop()    
        
        if not colour_sensor.value() == 1:
            ev3.Sound.speak('no black detected')
            left_motor.stop()
            right_motor.stop()
    

line_following()