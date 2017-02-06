import math


class CG3dVector(object):
    def __init__(self, x, y, z):
        self._data = [x, y, z]

    @property
    def data(self):
        return self._data

    def __str__(self):
        return str(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1] and self[2] == other[2]

    def add(self, other):
        return CG3dVector(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def sub(self, other):
        return CG3dVector(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def __rmul__(self, f):
        """
        scale
        """
        return CG3dVector(f * self[0], f * self[1], f * self[2])

    def scale(self, f):
        self._data[0] *= f
        self._data[1] *= f
        self._data[2] *= f

    def length(self):
        return math.sqrt(self._data[0]**2 + self._data[1]**2 + self._data[2]**2)

    def normalize(self):
        l = self.length()
        self._data[0] /= l
        self._data[1] /= l
        self._data[2] /= l

    def distance(self, other):
        return math.sqrt((self[0]-other[0])**2 + (self[1]-other[1])**2 + (self[2]-other[2])**2)

    def dot_product(self, other):
        return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]

    def cross_product(self, other):
        return CG3dVector(
            self[1] * other[2] - other[1] * self[2],
            self[2] * other[0] - other[2] * self[0],
            self[0] * other[1] - other[0] * self[1]
        )

    def transform(self, tf):
        return tf.applyto(self)

    __add__ = add     # overload operator '+'
    __sub__ = sub     # overload operator '-'
    __mul__ = dot_product    # overload operator '*'
    __xor__ = cross_product  # overload operator '^'
