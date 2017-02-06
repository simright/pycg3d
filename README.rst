pycg3d - a pure python package for Computational Geometry in 3D
=======================

This package provides functions in computational geometry like:
- Vector functions/operators like dot product, cross product etc;
- Transformation like translation, rotation, mirror etc;


**Highlights of this package**:

- Pure python;
- Minimal dependency;
- Friendly operators for building expressions(e.g. '+','-','*','^' operators for vectors);
- No graphics;

**Installation**:
>>> pip install pycg3d

**Usage**:
- **Vector**
.. code-block:: python
  # **class CG3dVector** defines a vector with three components(float numbers)
  >>> from pycg3d.cg3d_vector import CG3dVector
  >>> v1 = CG3dVector(1.0, 0.0, 0.0)
  >>> print v1
  [1.0, 0.0, 0.0]

  # Each component of the vector could be accessed by index
  >>> print v1[0], v1[1], v1[2]
  1.0 0.0 0.0
  >>> v1[1]=2.0
  >>> print v1
  [1.0, 2.0, 0.0]

  # '+' and '-' operators can be used for component-wise +/- of vectors
  >>> v1 = CG3dVector(1.0, 2.0, 3.0)
  >>> v2 = CG3dVector(1.0, 0.0, 2.0)
  >>> v3 = v1 + v2
  >>> type(v3)
  <class 'pycg3d.cg3d_vector.CG3dVector'>
  >>> print v3
  [2.0, 2.0, 5.0]
  >>> v4 = v1 - v2
  >>> type(v4)
  <class 'pycg3d.cg3d_vector.CG3dVector'>
  >>> print v4
  [0.0, 2.0, 1.0]

  # '*' operator can be used for dot product of vectors
  >>> va = CG3dVector(1.0, 0.0, 0.0)
  >>> vb = CG3dVector(2.0, 2.0, 0.0)
  >>> print va*vb
  2.0

  # '^' operator can be used for cross product of vectors
  >>> vx = CG3dVector(1.0, 0.0, 0.0)
  >>> vy = CG3dVector(0.0, 1.0, 0.0)
  >>> vz = vx^vy
  >>> type(vz)
  <class 'pycg3d.cg3d_vector.CG3dVector'>
  >>> print vz
  [0.0, 0.0, 1.0]

- **Point**
  # **class CG3dPoint** defines a point in 3D space with three float numbers(x,y,z)
  # **class CG3dPoint** is actually an alias of class **CG3dVector**. This means an instance of class **CG3dPoint** is also always an instance of class **CG3dVector**, and all members of **CG3dVector** also apply to **CG3dPoint**

.. code-block:: python
  from pycg3d.cg3d_vector import CG3dVector
  from pycg3d.cg3d_point import CG3dPoint
  >>> p1 = CG3dPoint(1.0, 0.0, 0.0)
  >>> isinstance(p1, CG3dPoint)
  True
  >>> isinstance(p1, CG3dVector)
  True
  >>> p2 = CG3dPoint(0.0, 1.0, 0.0)
  >>> v12 = p2 - p1
  >>> isinstance(p1, CG3dPoint)
  True
  >>> isinstance(p1, CG3dVector)
  True

- **Line**
  - Any class that defines a line in 3D space should subclass from **CG3dLine**
  - class **CG3dLine2P** defines a line with two points
.. code-block:: python
  >>> from pycg3d.cg3d_point import CG3dPoint
  >>> from pycg3d.cg3d_line import CG3dLine2P
  >>> p1 = CG3dPoint(1.0, 0.0, 0.0)
  >>> p2 = CG3dPoint(0.0, 1.0, 0.0)
  >>> line = CG3dLine2P(p1, p2)
  >>> type(line)
  <class 'pycg3d.cg3d_line.CG3dLine2P'>
  ```

- **Plane**
  - Any class that defines a plane in 3D space should subclass from **CGPlane**
  - class **CG3dPlane3P** defines a plane with 3 points in the plane
  - class **CG3dPlanePN** defines a plane with a point in the plane and a normal vector

- **Transformations**
  - Transformation can be used to transform points in 3D space (e.g. translation, rotation, mirror);
  - Each transformation can be defined as the instance of a transformation class.
  - Available transformations:
    - class CG3dTranslateTF: translation alone any direction;
    - class CG3dXtranslateTF/CG3dYtranslateTF/CG3dZtranslateTF: translation alone X/Y/Z-axis
    - class CG3dRotateTF: rotation about an arbitrary axis
    - class CG3dXrotateTF/CG3dYrotateTF/CG3dZrotateTF: rotation about X/Y/Z axis

  - Transformations could be chained;

  - Examples:
.. code-block:: python
    # Transformation alone X-axis, Y-axis
    >>> from pycg3d.cg3d_point import CG3dPoint
    >>> from pycg3d.cg3d_transformer import CG3dXtranslateTF, CG3dYtranslateTF
    >>> p1 = CG3dPoint(0.0, 0.0, 0.0)
    >>> tf1 = CG3dXtranslateTF(1.0)
    >>> p2 = p1.transform(tf1)
    >>> print p2
    [1.0, 0.0, 0.0]
    >>> tf2 = CG3dYtranslateTF(2.0)
    >>> p3 = p2.transform(tf2)
    >>> print p3
    [1.0, 2.0, 0.0]

    # chained transformations
    >>> p4 = p1.transform(tf1).transform(tf2)
    >>> print p4
    [1.0, 2.0, 0.0]
