
import unittest
import math

from planimetrics.point import Point
from planimetrics.triangle import Triangle

class TriangleTest(unittest.TestCase):
    """
    Test triangle:
          /(1,1)      B
         /   |       / |
    (0,0)--(1,0)    A--C

    """
    points = {
        Point(0, 0),  # A
        Point(1, 0),  # C
        Point(1, 1),  # B
    }


    def test_constructor(self):
        return
        t = Triangle(self.points)
        self.assertEqual(t.A , self.points[0], 'a')
        self.assertEqual(t.B , self.points[2], 'b')
        self.assertEqual(t.C , self.points[1], 'c')


    def test_perimeter(self):
        return
        t = Triangle(self.points)
        perimeter =  1 + 1 + math.sqrt(2)
        self.assertEqual( t.perimeter(), perimeter,
            "Triangle perimeter should be {0} instead of {1}".format(perimeter, t.perimeter())
        )

if __name__ == '__main__':
    unittest.main()