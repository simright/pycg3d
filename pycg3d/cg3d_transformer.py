from pycg3d import cg3d_plane


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
        point, norm = self._plane.get_point_and_normal()
        norm.normalize()
        return point - 2.0 * ((point - point) * norm) * norm
