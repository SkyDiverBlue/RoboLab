#!/usr/bin/env python3

from enum import IntEnum, unique
from typing import List, Optional, Tuple, Dict
# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE


@unique
class Direction(IntEnum):
    """ Directions in degrees """
    NORTH = 0
    EAST  = 90
    SOUTH = 180
    WEST  = 270


# simple alias, no magic here
Weight = int
""" 
    Weight of a given path (received from the server)
    value:  -1 if broken path 
            >0 for all other paths
            never 0
"""


class Planet:
    """ Contains the representation of the map and provides certain functions to manipulate it according to the specifications """

    def __init__(self):
        """ Initializes the data structure """
        self.target = None

    # example: add_path((0, 3, Direction.NORTH), (0, 3, Direction.WEST), 1)
    def add_path(self, start: Tuple[int, int, Direction], target: Tuple[int, int, Direction], weight: int):
        """ Adds a path defined by its start and end coordinates to the map and assigns the weight to it """
        pass

    """ 
        example: 
        get_paths() returns: { 
                                (0, 3): {
                                            Direction.NORTH: ((0, 3), Direction.WEST, 1), 
                                            Direction.EAST: ((1, 3), Direction.WEST, 2) 
                                        },
                                (1, 3): {
                                            Direction.WEST: ((0, 3), Direction.EAST, 2), 
                                            ... 
                                        }, 
                                ...
                              }
    """

    def get_paths(self) -> Dict[Tuple[int, int], Dict[Direction, Tuple[Tuple[int, int], Direction, Weight]]]:
        """ Returns all paths """
        pass

    # example: shortest_path((0,0), (2,2)) returns: [(0, 0, Direction.East), (1, 0, Direction.North)]
    # example: shortest_path((0,0), (1,2)) returns: None
    def shortest_path(self, start: Tuple[int, int], target: Tuple[int, int]) -> Optional[List[Tuple[int, int, Direction]]]:
        """ Returns a shortest path between two nodes """
        pass
