#!/usr/bin/env python3

import unittest
from planet import Direction, Planet


class PlanetTestCase(unittest.TestCase):
    def setUp(self):
        self.planet = Planet()


class TestPlanet(PlanetTestCase):
    """
        model a planet and implement test cases

        example planet:
        +--+
        |  |
        +-0,3------+
           |       |
          0,2-----2,2 (target)
           |      /
        +-0,1    /
        |  |    /
        +-0,0-1,0
           |
        (start)

    """
    def test_integrity(self):
        # were all paths added correctly to the planet
        # check if add_path() works by using get_paths()
        self.assertFail('implement me!')

    def test_empty_planet(self):
        self.assertFail('implement me!')

    def test_target_not_reachable(self):
        self.assertFail('implement me!')

    def test_shortest_path(self):
        self.planet.add_path((0, 0, Direction.NORTH), (0, 1, Direction.North), 1)
        self.planet.add_path((1, 0, Direction.EAST), (1, 0, Direction.EAST), 1)
        self.planet.add_path((1, 0, Direction.North), (2 , 2, Direction.North), 3)
        self.planet.add_path((2, 2, Direction.WEST), (0, 2, Direction.WEST), 5)
        self.planet.add_path((2, 2, Direction.NORTH), (2, 3, Direction.NORTH), 1)
        self.planet.add_path((0, 2, Direction.NORTH), (0, 3, Direction.NORTH) ,1)
        self.planet.add_path((0, 1, Direction.WEST), (0, 0, Direction.WEST), 1)
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.EAST), (1,0,Direction.NORTH)])
        # at least 2 possible paths
        self.assertFail('implement me!')

    def test_same_length(self):
        # at least 2 possible paths with the same weight
        self.assertFail('implement me!')

    def test_shortest_path_with_loop(self):
        # does the shortest path algorithm loop infinitely?
        # there is a shortest path
        self.assertFail('implement me!')

    def test_target_not_reachable_with_loop(self):
        # does the shortest path algorithm loop infinitely?
        # there is no shortest path
         

if __name__ == "__main__":
    unittest.main()
