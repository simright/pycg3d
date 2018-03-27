import math
import unittest

from pycg3d.cg3d_point import CG3dPoint
from pycg3d import utils


class TestUtils(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(
            utils.distance(CG3dPoint(1.0, 2.0, 3.0), CG3dPoint(4.0, 1.0, 2.0)),
            math.sqrt(11.0)
        )


if __name__ == "__main__":
    unittest.main()