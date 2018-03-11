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
   
    