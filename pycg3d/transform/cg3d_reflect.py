from pycg3d.transform.cg3d_transform import CG3dTransformer
from pycg3d import cg3d_plane
from pycg3d import utils


class CG3dReflectTF(CG3dTransformer):
    def __init__(self):
        super(CG3dReflectTF, self).__init__()


class CG3dPlaneMirrorTF(CG3dReflectTF):
    def __init__(self, plane):
        assert isinstance(plane, cg3d_plane.CGPlane)
        super(CG3dPlaneMirrorTF, self).__init__()
        self._plane = plane

    def applyto(self, point):
        """
        compute mirrored point to a plane
        :param point: input point
        :return: mirrored point of the input point to Plane self._plane
        """
        return utils.mirror_point_to_plane(point, self._plane)
