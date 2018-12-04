from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    # ABCMeta assures that the constructor for the class raises an error
    """Our own version of collections Sequence abstract class."""
    @abstractmethod
    def __len__(self):

    @abstractmethod
    def __getitem__(self, j):

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError("argument should be a class of Sequence")
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True
    def __lt__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError("argument should be a class of Sequence")
        if len(self) > len(other):
            return False
        for j in range(len(self)):
            if self[j] > other[j]:
                return False
        return True

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    def index(self, val):
        """Reutrn leftmost index at which val is found(or raise ValueError)"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence")

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

