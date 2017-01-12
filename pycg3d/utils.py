import math

from pycg3d.point import Point
from pycg3d.plane import Plane


def dist2p(p1, p2):
    """
    compute distance between two points
    :param p1: a list with 3 floats or Point or Vector
    :param p2: a list with 3 floats or Point or Vector
    :return:
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def mirror_point_to_plane(p1, pln):
    """
    compute mirrored point to a plane
    :param p1: input point
    :param pln: instance of class Plane
    :return: mirrored point of p1 to Plane pl
    """
    assert isinstance(pln, Plane)
    pn, norm = pln.get_point_and_normal()
    norm.normalize()
    p2 = p1-2.0*((p1-pn)*norm)*norm

    return Point(p2[0], p2[1], p2[2])
