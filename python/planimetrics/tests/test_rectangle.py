
import unittest

from planimetrics.point import Point
from planimetrics.rectangle import Rectangle

#@unittest.skip("Unsolved ordering of points")
class RectangleTest(unittest.TestCase):
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    p4 = Point(1, 1)

    def test_constructor(self):
        t = Rectangle({self.p1, self.p4})
        self.assertEqual(t.A, self.p1, "")
        #self.assertEqual(t.B, self.p2, "")
        self.assertEqual(t.C, self.p4, "")

    @unittest.skip("Unsolved ordering of points")
    def test_perimeter(self):
        t = Rectangle({self.p1, self.p4})
        perimeter = 4
        self.assertEqual( t.perimeter(), perimeter,
            "Rectangle perimeter should be {0} instead of {1}".format(perimeter, t.perimeter())
        )

if __name__ == '__main__':
    unittest.main()