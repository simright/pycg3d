import math
from pycg3d import cg3d_vector
from pycg3d import cg3d_plane


def vlength(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)


def distance(p1, p2):
    """
    compute distance between two points
    :param p1: point 1 defined as a list with 3 floats or CG3dPoint
    :param p2: point 2 defined as a list with 3 floats or CG3dPoint
    :return: float
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def dot_product(v1, v2):
    """
    compute dot production of two vectors
    :param v1: vector 1 (a list with 3 floats or CG3dVector)
    :param v2: vector 2 (a list with 3 floats or CG3dVector)
    :return: float
    """
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def cross_product(v1, v2):
    """
    compute cross production of two vectors
    :param v1: vector 1 (a list with 3 floats or CG3dVector)
    :param v2: vector 2 (a list with 3 floats or CG3dVector)
    :return: CG3dVector
    """
    return cg3d_vector.CG3dVector(
        v1[1] * v2[2] - v2[1] * v1[2],
        v1[2] * v2[0] - v2[2] * v1[0],
        v1[0] * v2[1] - v2[0] * v1[1]
    )


def mirror_point_to_plane(point, plane):
    """
    compute mirrored point to a plane
    :param point: input point (CG3dPoint)
    :param plane: mirror plane (CG3dPlane)
    :return: CG3dPoint
    """
    assert isinstance(plane, cg3d_plane.CGPlane)
    pn, norm = plane.get_point_and_normal()
    norm.normalize()
    return point - 2.0 * ((point - pn) * norm) * norm


def compute_angle_v2v(v1, v2, v3=None):
    """
    compute angle between two vectors, measured in radians within [0, pi) if v3 is not provided
    measured in radians within [0, 2*pi) if v3 is provided
    :param v1: Vector 1
    :param v2: Vector 2
    :param v3: Vector 3. User-defined direction that is used to define if the angle is bigger than pi
    :return: angle between Vectors v1 and v2, measured in radians within [0, pi) if v3 is not provided
                                                measured in radians within [0, 2*pi) if v3 is provided
    """

    alpha = math.acos(dot_product(v1, v2) / (vlength(v1)*vlength(v2)))
    if v3 is not None:
        cross = cross_product(v2, v1)
        if dot_product(cross,v3) > 0.0:
            return 2*math.pi-alpha

    return alpha


if __name__ == '__main__':
    a = [1.0, 1.0, 0.0]
    b = [1.0, -1.0, 0.0]
    c = [0.0, 0.0, 1.0]
    print(math.degrees(compute_angle_v2v(a,b)))
    print(math.degrees(compute_angle_v2v(a,b,c)))
    print(math.degrees(compute_angle_v2v(b, a, c)))
    print(compute_angle_v2v([1.0, 0.0, 0.0],[-1.0, 1.0, 0.0],[0.0,0.0,1.0]))