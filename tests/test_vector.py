import math

import unittest

from pycg3d.vector import Vector


class TestVector(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Vector(1.0, 0.0, 0.0), Vector(1.0, 0.0, 0.0))
        self.assertNotEqual(Vector(1.0, 0.0, 0.0), Vector(2.0, 0.0, 0.0))

    def test_add(self):
        self.assertEqual(Vector(1.0, 0.0, 0.0)+Vector(2.0, 3.0, 4.0), Vector(3.0, 3.0, 4.0))
        self.assertEqual(Vector(1.0, 0.0, 0.0).add(Vector(2.0, 3.0, 4.0)), Vector(3.0, 3.0, 4.0))

    def test_sub(self):
        self.assertEqual(Vector(1.0, 0.0, 6.0)-Vector(2.0, 3.0, 4.0), Vector(-1.0, -3.0, 2.0))
        self.assertEqual(Vector(1.0, 0.0, 6.0).sub(Vector(2.0, 3.0, 4.0)), Vector(-1.0, -3.0, 2.0))

    def test_dot_product(self):
        self.assertEqual(Vector(1.0, -1.0, 6.0)*Vector(2.0, 3.0, 4.0), 23.0)
        self.assertEqual(Vector(1.0, -1.0, 6.0).dot_product(Vector(2.0, 3.0, 4.0)), 23.0)

    def test_left_multiple(self):
        self.assertEqual(2.0*Vector(1.0, 2.0, 3.0), Vector(2.0, 4.0, 6.0))

    def test_scale(self):
        v = Vector(1.0, 2.0, 3.0)
        v.scale(2.0)
        self.assertEqual(v, Vector(2.0, 4.0, 6.0))

    def test_length(self):
        self.assertEqual(Vector(1.0, 2.0, 3.0).length(), math.sqrt(14.0))

    def test_cross_product(self):
        self.assertEqual(Vector(1.0, 0.0, 0.0)^Vector(0.0, 1.0, 0.0), Vector(0.0, 0.0, 1.0))
        self.assertEqual(Vector(1.0, 0.0, 0.0).cross_product(Vector(0.0, 1.0, 0.0)), Vector(0.0, 0.0, 1.0))

    def test_normalize(self):
        inputs = [
            [Vector(10.0, 0.0, 0.0), Vector(1.0, 0.0, 0.0)],
            [Vector(0.0, -2.0, 0.0), Vector(0.0, -1.0, 0.0)],
            [Vector(0.0, 0.0, 5.0),  Vector(0.0, 0.0, 1.0)],
        ]

        for v1, v2 in inputs:
            v1.normalize()
            self.assertEqual(v1, v2)
