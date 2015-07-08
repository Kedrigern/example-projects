from planimetrics.point import Point
from planimetrics.shape import Shape


class Rectangle(Shape):
    # todo: ordering of points
    # only two points

    def __init__(self, points):
        """
        :param points: 2 point at
        :return:
        """
        if len(points) != 2:
            raise Exception

        p = Shape._nearest_to_origin(points)
        self.A = p
        points.remove(p)
        self.C = points.pop()
        self.B = Point(self.A.y, self.C.x)
        self.D = Point(self.A.x, self.C.y)

    def perimeter(self):
        l1 = self.A.distance(self.B)
        l2 = self.B.distance(self.C)
        l3 = self.C.distance(self.D)
        l4 = self.D.distance(self.A)
        return l1 + l2 + l3 + l4

    def area(self):
        l1 = self.A.distance(self.B)
        l2 = self.A.distance(self.D)
        return l1 * l2
