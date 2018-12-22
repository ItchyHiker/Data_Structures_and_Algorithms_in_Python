import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplefied Python list
    using a raw array from ctypes module as storage
    """

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not k < self._n and k > -self._n:
            raise IndexError("invalid index")
        elif k > 0:
            return self._A[k]
        else:
            return self._A[k+self._n]

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _insert_resize(self, c, index, value):
        """resize for insert operation"""
        B = self._make_array(c)
        for i in range(index):
            B[i] = self._A[i]
        B[index] = value
        for i in range(index+1, self._n+1):
            B[i] = self._A[i-1]
        self._A = B
        self._capacity=c
        self._n += 1
    def _make_array(self, c):
        """return new array with capacity c"""
        return (c*ctypes.py_object)()   # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        if self._n == self._capacity:
            self._insert_resize(2*self._capacity, k, value)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
            self._A[k] = value
            self._n += 1 # add 1 to the size of the array

if __name__ == "__main__":
    a = DynamicArray()
    for i in range(10):
        a.append(i)
    a.insert(2, 100)



