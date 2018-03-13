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
        self.assertFail('implement me!')

    def test_empty_planet(self):
        self.assertIsNone(self.planet.shortest_path((0,0),(1,2)))


    def test_target_not_reachable(self):
        self.assertIsNone(self.planet.shortest_path((0,0),(1,2)))
        self.assertFail('implement me!')

    def test_shortest_path(self):
        self.planet.add_path((0, 0, Direction.EAST), (1, 0, Direction.West))
        self.planet.add_path((0, 1, Direction.North), (0, 2, Direction.South))
        self.planet.add_path((1, 0, Direction.North), (2, 2, Direction.South))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.East), (1,0,Direction.North)])
        self.assertFail('implement me!')

    def test_same_length(self):
        self.planet.add_path((0, 0, Direction.East), (1, 0, Direction.West))
        self.planet.add_path((0, 1, Direction.North), (0, 2, Direction.South))
        self.planet.add_path((0, 2, Direction.East), (2, 2, Direction.West))
        self.planet.add_path((1, 0, Direction.North), (2, 2, Direction.South))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.East), (1,0,Direction.North)])
        self.assertFail('implement me!')
   
        self.assertFail('implement me!')

    def test_shortest_path_with_loop(self):
        self.planet.add_path((0, 0, Direction.East), (1, 0, Direction.West))
        self.planet.add_path((0, 1, Direction.North), (0, 2, Direction.South))
        self.planet.add_path((0, 2, Direction.North), (0, 3, Direction.South))
        self.planet.add_path((0, 2, Direction.East), (2, 2, Direction.West))
        self.planet.add_path((0, 3, Direction.North), (0, 3, Direction.West))
        self.planet.add_path((0, 3, Direction.East), (2, 2, Direction.North))
        self.planet.add_path((1, 0, Direction.North), (2, 2, Direction.South))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.East), (1,0,Direction.North)])


        self.assertFail('implement me!')

    def test_target_not_reachable_with_loop(self):
        self.planet.add_path((0, 1, Direction.West), (0, 0, Direction.West))
        self.assertIsNone(self.planet.shortest_path((0, 0), (1, 2)))

if __name__ == "__main__":
    unittest.main()

class SecondPlanet(PlanetTestCase):
  #         +--------+      3,6---- +      
  #         |        |       |      |      
  #        0,5-------+       |      |     
  #         |                |      |      
  #        0,4              3,4----4,4----5,4
  #         |                |      |   /
  #        0,3--+            |      |  /
  #         |    \           |      | /
  #         |     \         3,2----4,2
  #         |      \         |
  #         |       \        |
  #         |        \       |
  #        0,0-------2,0----3,0
  #         |


    def test_1_empty_planet(self):
        self.assertIsNone(self.planet.shortest_path((0,3),(4,3)))

    def test_2_target_not_reachable(self):
        self.assertIsNone(self.planet.shortest_path((0,0),(3,3)))

    def test_shortest_path(self):
        self.planet.add_path((2, 0, Direction.East), (3, 0, Direction.West))
        self.planet.add_path((3, 0, Direction.North), (3, 2, Direction.South))
        self.planet.add_path((3, 2, Direction.North), (3, 4, Direction.South))
        self.planet.add_path((3, 4, Direction.North), (3, 6, Direction.South))
        self.planet.add_path((3, 6, Direction.North), (4, 4, Direction.North))
        self.planet.add_path((3, 6, Direction.East), (4, 4, Direction.East))
        self.planet.add_path((4, 4, Direction.East), (5, 4, Direction.West))
        self.planet.add_path((3, 2, Direction.East), (4, 2, Direction.West))
        self.planet.add_path((4, 2, Direction.East), (5, 4, Direction.South))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4)), [(2, 0, Direction.East), (3, 0, Direction.North)])

    def test_same_length(self):
        self.planet.add_path((2, 0, Direction.East), (3, 0, Direction.West))
        self.planet.add_path((3, 0, Direction.North), (3, 2, Direction.South))
        self.planet.add_path((3, 2, Direction.East), (4, 2, Direction.West))
        self.planet.add_path((3, 2, Direction.North), (3, 4, Direction.South))
        self.planet.add_path((4, 2, Direction.North), (4, 4, Direction.South))
        self.planet.add_path((0, 3, Direction.North), (0, 4, Direction.South))
        self.planet.add_path((0, 4, Direction.North), (0, 5, Direction.South))
        self.planet.add_path((3, 4, Direction.East), (4, 4, Direction.West))
        self.planet.add_path((3, 4, Direction.North), (3, 6, Direction.South))
        self.planet.add_path((4, 4, Direction.North), (3, 6, Direction.East))
        self.planet.add_path((4, 4, Direction.East), (5, 4, Direction.West))
        self.planet.add_path((4, 2, Direction.East), (5, 4, Direction.South))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4), [(2, 0, Direction.East), (3, 0, Direction.North)])

    def test_4_shortest_path_with_loop(self):
        self.planet.add_path((0, 0, Direction.East), (2, 0, Direction.West))
        self.planet.add_path((2, 0, Direction.East), (3, 0, Direction.West))
        self.planet.add_path((3, 0, Direction.North), (3, 2, Direction.South))
        self.planet.add_path((3, 2, Direction.East), (4, 2, Direction.West))
        self.planet.add_path((3, 2, Direction.North), (3, 4, Direction.South))
        self.planet.add_path((4, 2, Direction.North), (4, 4, Direction.South))
        self.planet.add_path((0, 3, Direction.North), (0, 4, Direction.South))
        self.planet.add_path((0, 4, Direction.North), (0, 5, Direction.South))
        self.planet.add_path((3, 4, Direction.East), (4, 4, Direction.West))
        self.planet.add_path((3, 4, Direction.North), (3, 6, Direction.South))
        self.planet.add_path((4, 4, Direction.North), (3, 6, Direction.East))
        self.planet.add_path((4, 4, Direction.East), (5, 4, Direction.West))
        self.planet.add_path((4, 2, Direction.East), (5, 4, Direction.South))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4)), [(0,0,Direction.East), (2,0,Direction.East), (3,0,Direction.North)])
   