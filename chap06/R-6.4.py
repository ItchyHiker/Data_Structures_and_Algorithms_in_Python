class Empty(Exception):
    pass
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    def remove(self):
        if self.is_empty():
            print("stack is empty")
            # return self
        else:
            self.pop().remove


def Transfer(s1, s2):
    if not s2.is_empty:
        raise ErrorSize("s2 must be empty")
    for i in range(len(s1)):
        s2.push(s1.pop())
def reverse(l):
    s = ArrayStack()
    n = len(l)
    for i in range(n):
        s.push(l[i])
    for i in range(n):
        l[i] = s.pop()
if __name__ == "__main__":
    s1 = ArrayStack()
    s2 = ArrayStack()
    for i in range(10):
        s1.push(i)
    Transfer(s1, s2)
    for i in range(10):
        print("s2 top:{}".format(s2.pop()))

    l = [5,7,2,9,3]
    reverse(l)
    print(l)

    s2.remove()
    if s2.is_empty():
        print("s2 is empty")

