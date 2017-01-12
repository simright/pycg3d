from pycg3d.point import Point


class Line(object):
    def __init__(self):
        pass


class Line2p(Line):
    """
    Line defined by two points
    """
    def __init__(self, p1, p2):
        assert isinstance(p1, Point)
        assert isinstance(p2, point)
        super(Line2p, self).__init__()
        self._p1 = p1
        self._p2 = p2

