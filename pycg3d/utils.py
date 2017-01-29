import math
from pycg3d import cg3d_point
from pycg3d import cg3d_vector
from pycg3d import cg3d_plane


def distance(p1, p2):
    """
    compute distance between two points
    :param p1: a list with 3 floats or Point or CG3dVector
    :param p2: a list with 3 floats or Point or CG3dVector
    :return:
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def cross_product(v1, v2):
    return cg3d_vector.CG3dVector(
        v1[1] * v2[2] - v2[1] * v1[2],
        v1[2] * v2[0] - v2[2] * v1[0],
        v1[0] * v2[1] - v2[0] * v1[1]
    )


def mirror_point_to_plane(point, plane):
    """

    :param point: input point
    :param plane: mirror plane
    :return: mirrored point
    """
    assert isinstance(plane, cg3d_plane.CGPlane)
    pn, norm = plane.get_point_and_normal()
    norm.normalize()
    return point - 2.0 * ((point - pn) * norm) * norm
