
from planimetrics.point import Point
from planimetrics.shape import Shape

class Triangle(Shape):

    def __init__(self, points):
        """
        :param points: set of three points
        :type points: set
        :return:
        """
        if len(points) != 3:
            raise Exception

        for p in points:
            if not isinstance(p, Point):
                raise Exception

        self._determineNodes(points)

    def _determineNodes(self, points):
        distances = {
            'e1': points[0].distance(points[1]),
            'e2': points[1].distance(points[2]),
            'e3': points[2].distance(points[3])
        }

        ec = max(distances, val = lambda record: distances[record])

        if ec == 'e1':
            self.C = points.pop(2)
        elif ec == 'e2':
            self.C = points.pop(0)
        elif ec == 'e3':
            self.C = points.pop(1)

        if points[0].x < points[1].x:
            self.A = points[0]
            self.B = points[1]
        else:
            self.A = points[1]
            self.B = points[0]

    def perimeter(self):
        l1 = self.A.distance(self.B)
        l2 = self.B.distance(self.C)
        l3 = self.C.distance(self.A)
        return l1 + l2 + l3

    def area(self):
        # todo area of triangle
        pass