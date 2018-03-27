import unittest

from pycg3d.cg3d_plane import CG3dPlane3P
from pycg3d.cg3d_point import CG3dPoint
from pycg3d.transform import cg3d_rotate
from pycg3d.transform import cg3d_reflect


class TestTransformers(unittest.TestCase):
    def test_mirror_point_to_plane(self):
        p1 = CG3dPoint(1.0, 0.0, 0.0)
        plane = CG3dPlane3P(
                    CG3dPoint(0.0, 0.0, 0.0),
                    CG3dPoint(0.0, 1.0, 0.0),
                    CG3dPoint(0.0, 0.0, 1.0),
                )
        mirror = cg3d_reflect.CG3dPlaneMirrorTF(plane)
        p2 = p1.transform(mirror)

        self.assertEqual(p2, CG3dPoint(-1.0, 0.0, 0.0))

    def test_rotate(self):
        tf = cg3d_rotate.CG3dZrotateTF(90.0)
        p1 = CG3dPoint(1.0, 0.0, 0.0)
        p2 = p1.transform(tf)
        self.assertAlmostEqual(p2[0], 0.0)
        self.assertAlmostEqual(p2[1], 1.0)
        self.assertAlmostEqual(p2[2], 0.0)


if __name__ == "__main__":
    unittest.main()
