import math

from pycg3d.cg3d_point import CG3dPoint
from pycg3d.cg3d_plane import CGPlane


def dist2p(p1, p2):
    """
    compute distance between two points
    :param p1: a list with 3 floats or Point or CG3dVector
    :param p2: a list with 3 floats or Point or CG3dVector
    :return:
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def mirror_point_to_plane(p1, pln):
    """
    compute mirrored point to a plane
    :param p1: input point
    :param pln: instance of class CGPlane
    :return: mirrored point of p1 to CGPlane pl
    """
    assert isinstance(pln, CGPlane)
    pn, norm = pln.get_point_and_normal()
    norm.normalize()
    p2 = p1-2.0*((p1-pn)*norm)*norm

    return CG3dPoint(p2[0], p2[1], p2[2])
