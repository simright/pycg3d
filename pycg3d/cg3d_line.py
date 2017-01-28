from pycg3d.cg3d_point import CG3dPoint


class CG3dLine(object):
    def __init__(self):
        pass


class CG3dLine2P(CG3dLine):
    """
    CG3dLine defined by two points
    """
    def __init__(self, p1, p2):
        assert isinstance(p1, CG3dPoint)
        assert isinstance(p2, CG3dPoint)
        super(CG3dLine2P, self).__init__()
        self._p1 = p1
        self._p2 = p2

