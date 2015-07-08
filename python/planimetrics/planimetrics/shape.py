from planimetrics.point import Point

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

    @staticmethod
    def _first_point(points):
        """
        Determinate point nearest to the origin ([0,0])

        :param points: Set of points
        :type points: Set
        :return: Point
        """
        if len(points) == 0:
            raise Exception

        for i in range(4):
            quadrant = [p for p in points if Shape._quadrant(p) == 1]
            if len(quadrant) > 0:
                return Shape._nearest_to_origin(quadrant)

    @staticmethod
    def _nearest_to_origin(points):
        min = Point.maxPoint()
        for p in points:
            if p.x == min.x:
                if p.y < min.y:
                    min = p
            elif p.x < min.x:
                min = p
        return min

    @staticmethod
    def _quadrant(point):
        """
        Determinate quadrant of the given point.
        Quadrants are:
         II | I
        ----|----
        III | IV
        :param point:
        :type point: Point
        :return: int in [1,2,3,4]
        """
        if point.y > 0:
            if point.x > 0:
                return 1
            else:
                return 2
        else:
            if point.x < 0:
                return 3
            else:
                return 4


