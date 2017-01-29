import math

import unittest

from pycg3d.cg3d_vector import CG3dVector


class TestVector(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(CG3dVector(1.0, 0.0, 0.0), CG3dVector(1.0, 0.0, 0.0))
        self.assertNotEqual(CG3dVector(1.0, 0.0, 0.0), CG3dVector(2.0, 0.0, 0.0))

    def test_add(self):
        self.assertEqual(CG3dVector(1.0, 0.0, 0.0) + CG3dVector(2.0, 3.0, 4.0), CG3dVector(3.0, 3.0, 4.0))
        self.assertEqual(CG3dVector(1.0, 0.0, 0.0).add(CG3dVector(2.0, 3.0, 4.0)), CG3dVector(3.0, 3.0, 4.0))

    def test_sub(self):
        self.assertEqual(CG3dVector(1.0, 0.0, 6.0) - CG3dVector(2.0, 3.0, 4.0), CG3dVector(-1.0, -3.0, 2.0))
        self.assertEqual(CG3dVector(1.0, 0.0, 6.0).sub(CG3dVector(2.0, 3.0, 4.0)), CG3dVector(-1.0, -3.0, 2.0))

    def test_left_multiple(self):
        self.assertEqual(2.0 * CG3dVector(1.0, 2.0, 3.0), CG3dVector(2.0, 4.0, 6.0))

    def test_scale(self):
        v = CG3dVector(1.0, 2.0, 3.0)
        v.scale(2.0)
        self.assertEqual(v, CG3dVector(2.0, 4.0, 6.0))

    def test_length(self):
        self.assertEqual(CG3dVector(1.0, 2.0, 3.0).length(), math.sqrt(14.0))

    def test_dot_product(self):
        self.assertEqual(CG3dVector(1.0, -1.0, 6.0) * CG3dVector(2.0, 3.0, 4.0), 23.0)
        self.assertEqual(CG3dVector(1.0, -1.0, 6.0).dot_product(CG3dVector(2.0, 3.0, 4.0)), 23.0)

    def test_cross_product(self):
        self.assertEqual(
            CG3dVector(1.0, 0.0, 0.0) ^ CG3dVector(0.0, 1.0, 0.0),
            CG3dVector(0.0, 0.0, 1.0)
        )
        self.assertEqual(
            CG3dVector(1.0, 0.0, 0.0).cross_product(CG3dVector(0.0, 1.0, 0.0)),
            CG3dVector(0.0, 0.0, 1.0)
        )

    def test_normalize(self):
        inputs = [
            [CG3dVector(10.0, 0.0, 0.0), CG3dVector(1.0, 0.0, 0.0)],
            [CG3dVector(0.0, -2.0, 0.0), CG3dVector(0.0, -1.0, 0.0)],
            [CG3dVector(0.0, 0.0, 5.0), CG3dVector(0.0, 0.0, 1.0)],
        ]

        for v1, v2 in inputs:
            v1.normalize()
            self.assertEqual(v1, v2)
