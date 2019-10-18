import math
import unittest

from pycg3d.cg3d_point import CG3dPoint
from pycg3d import utils


class TestUtils(unittest.TestCase):
    def test_vlenth(self):
        self.assertAlmostEqual(
            utils.vlength([1.0, 2.0, 3.0]),
            3.7416573867739413,
            delta=0.001
        )

    def test_distance(self):
        self.assertEqual(
            utils.distance(CG3dPoint(1.0, 2.0, 3.0), CG3dPoint(4.0, 1.0, 2.0)),
            math.sqrt(11.0)
        )

    def test_compute_angle_v2v(self):
        self.assertEqual(
            utils.compute_angle_v2v(
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0]
            ),
            0.5*math.pi
        )

        self.assertEqual(
            utils.compute_angle_v2v(
                [1.0, 0.0, 0.0],
                [-1.0, 1.0, 0.0]
            ),
            0.75*math.pi
        )

        self.assertEqual(
            utils.compute_angle_v2v(
                [1.0, 0.0, 0.0],
                [-1.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]
            ),
            0.75 * math.pi
        )

        self.assertEqual(
            utils.compute_angle_v2v(
                [1.0, 0.0, 0.0],
                [-1.0, 1.0, 0.0],
                [0.0, 0.0, -1.0]
            ),
            1.25 * math.pi
        )


if __name__ == "__main__":
    unittest.main()