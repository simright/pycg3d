class CGPlane(object):
    def __init__(self):
        pass

    def get_point_and_normal(self):
        raise NotImplementedError


class CG3dPlane3P(CGPlane):
    """
    CGPlane defined by 3 points (right hand, anti-clockwise)
    """
    def __init__(self, p1, p2, p3):
        super(CG3dPlane3P, self).__init__()
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def get_point_and_normal(self):
        return self._p1, (self._p2-self._p1)^(self._p3-self._p1)


class CG3dPlanePN(CGPlane):
    """
    CGPlane defined by point and normal
    """
    def __init__(self, pt, normal):
        super(CG3dPlanePN, self).__init__()
        self._pt = pt
        self._normal = normal

    def get_point_and_normal(self):
        return self._pt, self._normal
