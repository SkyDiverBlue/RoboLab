#!/usr/bin/env python3

from enum import IntEnum, unique
from typing import List, Optional, Tuple, Dict

# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class Direction(IntEnum):
    NORTH=0
    EAST=90
    SOUTH=180
    WEST=270

class Planet:
   
    def relative_orientation(self): #defines compass direction after turn
        if orientation == 0:
            if linefollowing.turn_to_right_intersection(self):
                orientation = 1
            if linefollowing.turn_to_left_intersection(self):
                orientation = 3
            else:
                orientation = 0
        if orientation == 1:
            if linefollowing.turn_to_right_intersection(self):
                orientation = 2
            if linefollowing.turn_to_left_intersection(self):
                orientation = 0
            else:
                orientation = 1
        if orientation == 2:
            if linefollowing.turn_to_right_intersection(self):
                orientation = 3
            if linefollowing.turn_to_left_intersection(self):
                orientation = 1
            else:
                orientation = 2
        if orientation == 3:
            if linefollowing.turn_to_right_intersection(self):
                orientation = 0
            if linefollowing.turn_to_left_intersection(self):
                orientation = 2
            else:
                orientation = 3



