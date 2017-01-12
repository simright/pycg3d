class Plane(object):
    def __init__(self):
        pass

    def get_point_and_normal(self):
        raise NotImplementedError


class PlaneBy3Points(Plane):
    """
    Plane defined by 3 points (right hand, anti-clockwise)
    """
    def __init__(self, p1, p2, p3):
        super(PlaneBy3Points, self).__init__()
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def get_point_and_normal(self):
        return self._p1, (self._p2-self._p1)^(self._p3-self._p1)


class PlaneByPointNormal(Plane):
    """
    Plane defined by point and normal
    """
    def __init__(self, pt, normal):
        super(PlaneByPointNormal, self).__init__()
        self._pt = pt
        self._normal = normal

    def get_point_and_normal(self):
        return self._pt, self._normal
