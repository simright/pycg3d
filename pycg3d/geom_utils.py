from pycg3d.cg3d_point import CG3dPoint


def compute_tetra_vol(p0, p1, p2, p3):
    assert isinstance(p0, CG3dPoint)
    assert isinstance(p1, CG3dPoint)
    assert isinstance(p2, CG3dPoint)
    assert isinstance(p3, CG3dPoint)
    vec01 = p1 - p0
    vec02 = p2 - p0
    vec03 = p3 - p0

    return ((vec01^vec02)*vec03)/6.0
