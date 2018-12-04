class Vector:
    """Represent a vector in a multidimensional space"""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0]*d
        else:
            self._coords = list(d)
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, val):
        self._coords[j] = val
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self._coords[j]*other
        elif isinstance(other, Vector):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self._coords[j]*other._coords[j]
        else:
            raise TypeError("left operand must be int float or a Vector instance")
        return result
    def __rmul__(self, n):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self._coords[j]* n
        return result
    def __neg__(self):
        result = Vector(len(self))
        result -= self
        return result
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self, other):
        return not self == other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == "__main__":
    v1 = Vector(3)
    v1[0] = 1
    v1[1] = 2
    v1[2] = 3
    v2 = Vector(3)
    v2[0] = 4
    v2[1] = 5
    v2[2] = 6

    print(v2 - v1)
    print(-v2)
    print([1,2,3] + v2)
    print(v2*3)
    print(3*v2)
    print(v1*v2)
    print(Vector([1,2,3]))
