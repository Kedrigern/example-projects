
import unittest

from planimetrics.line import Line

class LineTest(unittest.TestCase):
    def test_construct(self):
        l = Line((0,0), (1,0))
        self.assertEqual(str(l.start), "[0, 0]")
        self.assertEqual(l.distance(), 1)
        self.assertEqual(l.angle(), 0)

if __name__ == '__main__':
    unittest.main()