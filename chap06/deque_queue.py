from collections import deque

class Empty(Exception):
    pass
class DequeQueue:
    """FIFO queue implementation using a Python list as underlying storage"""
    DEFAULT_CAPACITY=10

    def __init__(self):
        """Create an empty queue"""
        self._data = deque()
        self._size = len(self._data)

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data.popleft()
        self._size = len(self._data)
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue"""
        self._data.append(e)
        self._size = len(self._data)
if __name__ == "__main__":
    dq = DequeQueue()
    for i in range(10):
        dq.enqueue(i)
        print("length of dq:{}".format(len(dq)))
    for i in range(10):
        print("eleemnts dequeued:{}".format(dq.dequeue()))
        print("length of dq:{}".format(len(dq)))


