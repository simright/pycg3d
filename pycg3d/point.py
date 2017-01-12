from pycg3d.vector import Vector


class Point(Vector):
    def __init__(self, x, y, z):
        super(Point, self).__init__(x, y, z)
