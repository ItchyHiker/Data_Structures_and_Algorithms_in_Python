class CircularQueue:
    """Queue implementation using circularly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_elements', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            raise Exception("Queue is empty")
        old_head = self._tail._next
        if self._size = 1:
            self._tail=None
        else:
            self._tail._next=old_head._next
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self.tail.next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next

