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
        self.planet.add_path((0, 0, Direction.EAST), (1, 0, Direction.WEST), 1)
        self.planet.add_path((0, 1, Direction.NORTH), (0, 2, Direction.SOUTH), 2)
        self.planet.add_path((0, 0, Direction.NORTH), (0, 1, Direction.SOUTH), 3)
        
        a = {
              (0,0):{
                 Direction.EAST: ((1,0), Direction.WEST, 1),
                 Direction.NORTH: ((0,1), Direction.SOUTH, 3)
                 },
             (0,1):{
                 Direction.SOUTH: ((0,0), Direction.NORTH, 3),
                 Direction.NORTH: ((0,2), Direction.SOUTH, 2)
                 },
             (1,0):{
                 Direction.WEST: ((0,0), Direction.EAST, 1)
                 },
             (0,2):{
                 Direction.SOUTH: ((0,1), Direction.NORTH, 2)
                 }
            }
        self.assertEqual(self.planet.get_paths(), a)
    
    def test_empty_planet(self):
        self.assertIsNone(self.planet.shortest_path((0,0),(1,2)))


    def test_target_not_reachable(self):
        self.assertIsNone(self.planet.shortest_path((0,0),(1,2)))
        self.assertFail('implement me!')

    def test_shortest_path(self):
        self.planet.add_path((0, 0, Direction.EAST), (1, 0, Direction.WEST))
        self.planet.add_path((0, 1, Direction.NORTH), (0, 2, Direction.SOUTH))
        self.planet.add_path((1, 0, Direction.NORTH), (2, 2, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.EAST), (1,0,Direction.NORTH)])
        self.assertFail('implement me!')

    def test_same_length(self):
        self.planet.add_path((0, 0, Direction.EAST), (1, 0, Direction.WEST))
        self.planet.add_path((0, 1, Direction.NORTH), (0, 2, Direction.SOUTH))
        self.planet.add_path((0, 2, Direction.EAST), (2, 2, Direction.WEST))
        self.planet.add_path((1, 0, Direction.NORTH), (2, 2, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.EAST), (1,0,Direction.NORTH)])
        self.assertFail('implement me!')
   
        self.assertFail('implement me!')

    def test_shortest_path_with_loop(self):
        self.planet.add_path((0, 0, Direction.EAST), (1, 0, Direction.WEST))
        self.planet.add_path((0, 1, Direction.NORTH), (0, 2, Direction.SOUTH))
        self.planet.add_path((0, 2, Direction.NORTH), (0, 3, Direction.SOUTH))
        self.planet.add_path((0, 2, Direction.EAST), (2, 2, Direction.WEST))
        self.planet.add_path((0, 3, Direction.NORTH), (0, 3, Direction.WEST))
        self.planet.add_path((0, 3, Direction.EAST), (2, 2, Direction.NORTH))
        self.planet.add_path((1, 0, Direction.NORTH), (2, 2, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.EAST), (1,0,Direction.NORTH)])


        self.assertFail('implement me!')

    def test_target_not_reachable_with_loop(self):
        self.planet.add_path((0, 1, Direction.WEST), (0, 0, Direction.WEST))
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
        self.planet.add_path((2, 0, Direction.EAST), (3, 0, Direction.WEST))
        self.planet.add_path((3, 0, Direction.NORTH), (3, 2, Direction.SOUTH))
        self.planet.add_path((3, 2, Direction.NORTH), (3, 4, Direction.SOUTH))
        self.planet.add_path((3, 4, Direction.NORTH), (3, 6, Direction.SOUTH))
        self.planet.add_path((3, 6, Direction.NORTH), (4, 4, Direction.NORTH))
        self.planet.add_path((3, 6, Direction.EAST), (4, 4, Direction.EAST))
        self.planet.add_path((4, 4, Direction.EAST), (5, 4, Direction.WEST))
        self.planet.add_path((3, 2, Direction.EAST), (4, 2, Direction.WEST))
        self.planet.add_path((4, 2, Direction.EAST), (5, 4, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4)), [(2, 0, Direction.EAST), (3, 0, Direction.NORTH)])

    def test_same_length(self):
        self.planet.add_path((2, 0, Direction.EAST), (3, 0, Direction.WEST))
        self.planet.add_path((3, 0, Direction.NORTH), (3, 2, Direction.SOUTH))
        self.planet.add_path((3, 2, Direction.EAST), (4, 2, Direction.WEST))
        self.planet.add_path((3, 2, Direction.NORTH), (3, 4, Direction.SOUTH))
        self.planet.add_path((4, 2, Direction.NORTH), (4, 4, Direction.SOUTH))
        self.planet.add_path((0, 3, Direction.NORTH), (0, 4, Direction.SOUTH))
        self.planet.add_path((0, 4, Direction.NORTH), (0, 5, Direction.SOUTH))
        self.planet.add_path((3, 4, Direction.EAST), (4, 4, Direction.WEST))
        self.planet.add_path((3, 4, Direction.NORTH), (3, 6, Direction.SOUTH))
        self.planet.add_path((4, 4, Direction.NORTH), (3, 6, Direction.EAST))
        self.planet.add_path((4, 4, Direction.EAST), (5, 4, Direction.WEST))
        self.planet.add_path((4, 2, Direction.EAST), (5, 4, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4)), [(2, 0, Direction.EAST), (3, 0, Direction.NORTH)])

    def test_4_shortest_path_with_loop(self):
        self.planet.add_path((0, 0, Direction.EAST), (2, 0, Direction.WEST))
        self.planet.add_path((2, 0, Direction.EAST), (3, 0, Direction.WEST))
        self.planet.add_path((3, 0, Direction.NORTH), (3, 2, Direction.SOUTH))
        self.planet.add_path((3, 2, Direction.EAST), (4, 2, Direction.WEST))
        self.planet.add_path((3, 2, Direction.NORTH), (3, 4, Direction.SOUTH))
        self.planet.add_path((4, 2, Direction.NORTH), (4, 4, Direction.SOUTH))
        self.planet.add_path((0, 3, Direction.NORTH), (0, 4, Direction.SOUTH))
        self.planet.add_path((0, 4, Direction.NORTH), (0, 5, Direction.SOUTH))
        self.planet.add_path((3, 4, Direction.EAST), (4, 4, Direction.WEST))
        self.planet.add_path((3, 4, Direction.NORTH), (3, 6, Direction.SOUTH))
        self.planet.add_path((4, 4, Direction.NORTH), (3, 6, Direction.EAST))
        self.planet.add_path((4, 4, Direction.EAST), (5, 4, Direction.WEST))
        self.planet.add_path((4, 2, Direction.EAST), (5, 4, Direction.SOUTH))
        self.assertEqual(self.planet.shortest_path((2, 0), (5, 4)), [(0,0,Direction.EAST), (2,0,Direction.EAST), (3,0,Direction.NORTH)])
   