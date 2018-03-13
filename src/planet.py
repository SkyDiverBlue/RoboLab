#!/usr/bin/env python3

from enum import IntEnum, unique
from typing import List, Optional, Tuple, Dict
from collections import Counter

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
        self.start_point = (0,0)

        self.node = {}

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, value):
        self.start_point = value

    def add_path(self, start: Tuple[int, int, Direction], target: Tuple[int, int, Direction], weight: int):
                
        start_x, start_y, start_dir = start
        target_x, target_y, target_dir = target
        target_coordinates = (target_x, target_y)
        start_coordinates = (start_x,start_y)
        
        if start_coordinates not in self.node:
            self.node[start_coordinates] = {}

        if target_coordinates not in self.node:
            self.node[target_coordinates] = {}
        
        start_dict = self.node[start_coordinates]
        start_dict[start_dir] = (target_coordinates, target_dir, weight)

        start_dict = self.node[target_coordinates]
        start_dict[target_dir] = (start_coordinates, start_dir, weight)


    def get_paths(self) -> Dict[Tuple[int, int], Dict[Direction, Tuple[Tuple[int, int], Direction, Weight]]]:
        return self.node
    
    def shortest_path(self, start: Tuple[int, int], target: Tuple[int, int]) -> Optional[List[Tuple[int, int, Direction]]]:
        """ Returns a shortest path between two nodes """
              #NEED HELP PLS!!!     
        if self.node in self.start_dict:
            return []

    def dijkstra(self, graph):

        distance = {}
        updated_distance

        predecessor = {}
        visited = []
        univisited = {}
           
        if self.node == self.start_dict[1]:
            path = []
            self.start_dict[1] = previous_node
            while previous_node is not None:
                path.append(previous_node)
                previous_node = predecessor.get(previous_node, None)
            return Path

        else:
            if not visited:
                distance[self.node] = 0
            for self.start_dict[1] in graph[self.node]: #not sure of syntax
                if self.start_dict[1] not in visited:
                    
                    updated_distance = distance + self.start_dict[1]
                    if updated_distance < distance.get(self.start_dict[1]):
                        distances[self.start_dict[1]] = updated_distance
                        predecessor[self.start_dict[1]] = self.node
            visited.append(self.start_dict[1])
            


        

    





