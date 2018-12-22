from priority_queue_base imoprt PriorityQueueBase:
from .. import PositionalList
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        if self.is_empty(self):
            """Return position of item with minimum key"""
            if self.is_empty():
                raise Empty("priority queue is empty")
            small = self._data.first()
            walk = self._data.after(small)
            while walk is not None:
                if walk.element() < small.element():
                    small = walk
                walk = self._data.after(walk)
            return small

        def __init__(self):
            self._data = PositionalList()

        def __len__(self):
            return len(self._data)

        def add(self, key, value):
            self._data.add_last(self._Item(key, value))

        def min(self):
            p = self._find_min()
            item = p.element()
            return item._key, item._value

