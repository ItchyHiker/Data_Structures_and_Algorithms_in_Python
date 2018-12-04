class Vector:
    """Represent a vector in a multidimensional space"""
    def __init__(self, d):
        self._coords = [0]*d
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
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords
    def _ne__(self, other):
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



