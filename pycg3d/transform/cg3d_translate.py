from pycg3d.transform.cg3d_transform import CG3dTransformer


class CG3dTranslateTF(CG3dTransformer):
    def __init__(self, tx=0.0, ty=0.0, tz=0.0, cords=None):
        """

        :param tx: movement along X-axis
        :param ty: movement along Y-axis
        :param tz: movement along Z-axis
        :param cords: local coordinate system for the specified movement (None means global system)
        """
        super(CG3dTranslateTF, self).__init__()
        self._tx = tx
        self._ty = ty
        self._tz = tz
        self._cords = cords

        self._dv = None

    def get_dv(self):
        if self._dv is None:
            dv = cg3d_vector.CG3dVector(self._tx, self._ty, self._tz)
            if self._cords:
                assert isinstance(self._cords, cg3d_cords.CG3dCordsBase)
                dv = self._tx * self._cords.ex + \
                     self._ty * self._cords.ey + \
                     self._tz * self._cords.ez
            self._dv = dv
        return self._dv

    def applyto(self, point):
        return point + self.get_dv()


class CG3dXtranslateTF(CG3dTranslateTF):
    def __init__(self, tx, cords=None):
        super(CG3dXtranslateTF, self).__init__(tx=tx, cords=cords)


class CG3dYtranslateTF(CG3dTranslateTF):
    def __init__(self, ty, cords=None):
        super(CG3dYtranslateTF, self).__init__(ty=ty, cords=cords)


class CG3dZtranslateTF(CG3dTranslateTF):
    def __init__(self, tz, cords=None):
        super(CG3dZtranslateTF, self).__init__(tz=tz, cords=cords)
