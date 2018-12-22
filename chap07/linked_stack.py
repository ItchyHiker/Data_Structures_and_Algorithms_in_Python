class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #-------------- stack methods -------------
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        reutrn self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head) # 原始self._head变为next
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self._head._element # top of stack is at head of list

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer




