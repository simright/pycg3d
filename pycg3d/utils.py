import math


def dist2p(p1, p2):
    """
    compute distance between two points
    :param p1: a list with 3 floats or Point or CG3dVector
    :param p2: a list with 3 floats or Point or CG3dVector
    :return:
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
