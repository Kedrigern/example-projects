
from planimetrics.point import Point

class Line:

    def __init__(self, start, end):
        if isinstance(start, tuple):
            self.start = Point(start[0],start[1])
        else:
            self.start = start
        if isinstance(end, tuple):
            self.end = Point(end[0], end[1])
        else:
            self.end = end

    def distance(self):
        return self.start.distance(self.end)

    def angle(self):
        return self.start.angle(self.end)

    # todo: směrnicová rovnice přímky