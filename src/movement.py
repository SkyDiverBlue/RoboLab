

class Movement: 
    def __init__(self, motor_list):
        self.left_motor, self.right_motor = motor_list

    #run timed
    
    def forward_run_timed(self, t, s):
        self.left_motor.run_timed(time_sp = t, speed_sp = s) 
        self.right_motor.run_timed(time_sp = t, speed_sp= s)
    
    def tright_run_timed(self, t, s):
        self.right_motor.run_timed(time_sp= t, speed_sp = -s) 
        self.left_motor.run_timed(time_sp=t, speed_sp= s)
    
    def tleft_run_timed(self, t, s):
        self.right_motor.run_timed(time_sp= t, speed_sp = s) 
        self.left_motor.run_timed(time_sp=t, speed_sp= -s)

    def ttright_run_timed(self, t, s1, s2): #for PID controller
        self.right_motor.run_timed(time_sp= t, speed_sp = s1) 
        self.left_motor.run_timed(time_sp=t, speed_sp= s2)

    def ttleft_run_timed(self, t, s1, s2): #for PID controller
        self.left_motor.run_timed(time_sp= t, speed_sp = s1) 
        self.right_motor.run_timed(time_sp=t, speed_sp= s2)
    
    def stop_run_timed(self):
        self.left_motor.stop()
        self.right_motor.stop()

    #run relative position
    
    def turn_left_relpos(self, p, s):
        self.right_motor.run_to_rel_pos(position_sp = p, speed_sp = s)

    def turn_right_relpos(self, p, s):
        self.left_motor.run_to_rel_pos(position_sp = p, speed_sp = s)
         
    def forward_relpos(self, p , s):
        self.left_motor.run_to_rel_pos(position_sp = p, speed_sp = s)
        self.right_motor.run_to_rel_pos(position_sp = p, speed_sp = s)

    def tturn_right_relpos(self, p, s):
        self.left_motor.run_to_rel_pos(position_sp = p, speed_sp = s)
        self.right_motor.run_to_rel_pos(position_sp = -p, speed_sp = s)

    def tturn_left_relpos(self, p, s):
        self.left_motor.run_to_rel_pos(position_sp = -p, speed_sp = s)
        self.right_motor.run_to_rel_pos(position_sp = p, speed_sp = s)

    def  tturn_left_relpos(self, p, s):
        self.left_motor.run_to_rel_pos(position_sp = p, speed_sp = s)
        self.right_motor.run_to_rel_pos(position_sp = -p, speed_sp = s)

        
    def get_right_pos(self):
        self.right_motor.position

    def get_left_pos(self):
        self.left_motor.position

    
