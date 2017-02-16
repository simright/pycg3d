import math

from pycg3d import cg3d_point
from pycg3d import cg3d_vector
from pycg3d.transform.cg3d_transform import CG3dTransformer


class CG3dRotateTF(CG3dTransformer):
    def __init__(self, point, vector, angle):
        """
        :param point: base point of the rotation axis
        :param vector: vector of the rotation axis
        :param angle: rotation angle in degree
        """
        assert isinstance(point,  cg3d_point.CG3dPoint)
        assert isinstance(vector, cg3d_vector.CG3dVector)
        super(CG3dRotateTF, self).__init__()
        self._point = point
        self._vector = vector
        self._vector.normalize()
        self._angle = angle*math.pi/180.0

        self._matrix = None

    def get_matrix(self):
        if not self._matrix:
            # http://inside.mines.edu/fs_home/gmurray/ArbitraryAxisRotation/
            u, v, w = self._vector
            a, b, c = self._point
            cosT = math.cos(self._angle)
            sinT = math.sin(self._angle)

            self._matrix = [
                [
                    u ** 2 + (v ** 2 + w ** 2) * cosT,
                    u * v * (1.0 - cosT) - w * sinT,
                    u * w * (1.0 - cosT) + v * sinT,
                    (a * (v ** 2 + w ** 2) - u * (b * v + c * w)) * (1.0 - cosT) + (b * w - c * v) * sinT
                ],

                [
                    u * v * (1.0 - cosT) + w * sinT,
                    v ** 2 + (u ** 2 + w ** 2) * cosT,
                    v * w * (1 - cosT) - u * sinT,
                    (b * (u ** 2 + w ** 2) - v * (a * u + c * w)) * (1.0 - cosT) + (c * u - a * w) * sinT
                ],

                [
                    u * w * (1.0 - cosT) - v * sinT,
                    v * w * (1 - cosT) + u * sinT,
                    w ** 2 + (u ** 2 + v ** 2) * cosT,
                    (c * (u ** 2 + v ** 2) - w * (a * u + b * v)) * (1 - cosT) + (a * v - b * u) * sinT
                ],
                #[0.0, 0.0, 0.0, 1.0]
            ]

        return self._matrix

    def applyto(self, point):
        mtx = self.get_matrix()
        x = mtx[0][0]*point[0] + mtx[0][1]*point[1] + mtx[0][2]*point[2] + mtx[0][3]
        y = mtx[1][0]*point[0] + mtx[1][1]*point[1] + mtx[1][2]*point[2] + mtx[1][3]
        z = mtx[2][0]*point[0] + mtx[2][1]*point[1] + mtx[2][2]*point[2] + mtx[2][3]
        return cg3d_point.CG3dPoint(x, y, z)


class CG3dXrotateTF(CG3dRotateTF):
    def __init__(self, angle, cords=None):
        """
            rotate about X-axis
        :param angle:
        :param cords:
        """
        if not cords:
            point = cg3d_point.CG3dPoint(0.0, 0.0, 0.0)
            vector = cg3d_point.CG3dVector(1.0, 0.0, 0.0)
        else:
            point = cords.origin
            vector = cords.ex

        super(CG3dXrotateTF, self).__init__(point, vector, angle)


class CG3dYrotateTF(CG3dRotateTF):
    def __init__(self, angle, cords=None):
        """
            rotate about Y-axis
        :param angle:
        :param cords:
        """
        if not cords:
            point = cg3d_point.CG3dPoint(0.0, 0.0, 0.0)
            vector = cg3d_point.CG3dVector(0.0, 1.0, 0.0)
        else:
            point = cords.origin
            vector = cords.ey

        super(CG3dYrotateTF, self).__init__(point, vector, angle)


class CG3dZrotateTF(CG3dRotateTF):
    def __init__(self, angle, cords=None):
        """
            rotate about Z-axis
        :param angle:
        :param cords:
        """
        if not cords:
            point = cg3d_point.CG3dPoint(0.0, 0.0, 0.0)
            vector = cg3d_point.CG3dVector(0.0, 0.0, 1.0)
        else:
            point = cords.origin
            vector = cords.ez

        super(CG3dZrotateTF, self).__init__(point, vector, angle)
