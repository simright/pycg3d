from pycg3d import cg3d_vector
from pycg3d import cg3d_plane
from pycg3d import utils


class CG3dTransformer(object):
    def __init__(self):
        pass

    def applyto(self, ent):
        raise NotImplementedError


class CG3dMirrorTF(CG3dTransformer):
    def __init__(self, plane):
        assert isinstance(plane, cg3d_plane.CGPlane)
        super(CG3dMirrorTF, self).__init__()
        self._plane = plane

    def applyto(self, point):
        """
        compute mirrored point to a plane
        :param point: input point
        :return: mirrored point of the input point to Plane self._plane
        """
        return utils.mirror_point_to_plane(point, self._plane)


class CG3dRotateTF(CG3dTransformer):
    def __init__(self, point, vector, angle):
        super(CG3dRotateTF, self).__init__()
        self._point = point
        self._vector = vector
        self._angle = angle

    def applyto(self, ent):
        raise NotImplementedError


class CG3dTranslateTF(CG3dTransformer):
    def __init__(self, tx=0.0, ty=0.0, tz=0.0):
        super(CG3dTranslateTF, self).__init__()
        self._tx = tx
        self._ty = ty
        self._tz = tz

    def applyto(self, point):
        return point + cg3d_vector.CG3dVector(self._tx, self._ty, self._tz)
