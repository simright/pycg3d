from pycg3d import cg3d_vector
from pycg3d import utils


class CG3dCordsBase(object):
    def __init__(self):
        pass

    @property
    def origin(self):
        raise NotImplementedError

    @property
    def ex(self):
        raise NotImplementedError

    @property
    def ey(self):
        raise NotImplementedError

    @property
    def ez(self):
        raise NotImplementedError


class CG3dRectCords(CG3dCordsBase):
    def __init__(
            self,
            origin,
            ex=None,
            ey=None,
            ez=None,
            px=None,
            py=None,
            pz=None,
            pxy=None,
            pyz=None,
            pzx=None
    ):
        """

        :param origin: origin point of the axis
        :param ex:  vector of X-axis (from origin)
        :param px:  one point on X-axis
        :param ey:  vector of Y-axis
        :param py:  one point on Y-axis
        :param ez:  vector of Z-axis
        :param pz:  one point on Z-axis
        :param pxy: one point on XY plane
        :param pyz: one point on YZ plane
        :param pzx: one point on ZX plane
        """
        self._origin = origin
        self._ex = self.fix_cords(origin, ex, ey, ez, px, py, pz, pxy, pyz, pzx)
        self._ey = self.fix_cords(origin, ey, ez, self._ex, py, pz, px, pyz, pzx, pxy)
        self._ez = self.fix_cords(origin, ez, self._ex, self._ey, pz, px, py, pzx, pxy, pyz)

        self._ex.nornalize()
        self._ey.normalize()
        self._ez.normalize()

    def fix_cords(self, origin, e1, e2, e3, p1, p2, p3, p12, p23, p31):
        """
        fix e1
        :param origin:
        :param e1: vector of axis-1 or None
        :param e2: vector of axis-2 or None
        :param e3: vector of axis-3 or None
        :param p1: one point on axis-1 or None
        :param p2: one point on axis-2 or None
        :param p3: one point on axis-3 or None
        :param p12: one point on plane 12 or None
        :param p23: one point on plane 23 or None
        :param p31: one point on plane 31 or None
        :return:
        """
        assert isinstance(origin, cg3d_vector.CG3dVector)

        if e1:
            assert isinstance(e1, cg3d_vector.CG3dVector)
            return e1

        if p1:
            assert isinstance(p1, cg3d_vector.CG3dVector)
            return p1-origin

        # e1 is not defined
        if e2:
            if e3:
                return utils.cross_product(e2, e3)
            elif p3:
                return utils.cross_product(e2, p3-origin)
            elif p23:
                return utils.cross_product(e2, p3-origin)
            else:
                raise ValueError
        elif p2:
            return self.fix_cords(origin, e1, p2-origin, e3, p1, p2, p3, p12, p23, p31)
        else:
            raise ValueError

    @property
    def origin(self):
        return self._origin

    @property
    def ex(self):
        return self._ex

    @property
    def ey(self):
        return self._ey

    @property
    def ez(self):
        return self._ez
