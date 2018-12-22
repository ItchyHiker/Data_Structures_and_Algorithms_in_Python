class PriorityQueueBase:
    """Abstract base class for a priority queue"""
    class _Item:
        """Lightweight composite to store priority queue items
        use composite design pattern"""

        __slots__ = "_keys", "_value"
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """Compare items based on their keys"""
            return self._key < other._key

        def is_empty(self):
            """Return True is the priority is empty"""
            return len(self) == 0


