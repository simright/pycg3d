import math

import unittest

from pycg3d.point import Point
from pycg3d.plane import PlaneBy3Points, PlaneByPointNormal

from pycg3d import utils


class TestUtils(unittest.TestCase):
    def test_dis2p(self):
        self.assertEqual(
            utils.dist2p(Point(1.0, 2.0, 3.0), Point(4.0, 1.0, 2.0)),
            math.sqrt(11.0)
        )

    def test_mirror_point_to_plane(self):
        self.assertEqual(
            utils.mirror_point_to_plane(
                Point(1.0, 0.0, 0.0),
                PlaneBy3Points(
                    Point(0.0, 0.0, 0.0),
                    Point(0.0, 1.0, 0.0),
                    Point(0.0, 0.0, 1.0),
                )
            ),
            Point(-1.0, 0.0, 0.0)
        )