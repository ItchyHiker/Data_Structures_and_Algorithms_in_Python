from favorite_list import FavoriteList

class FavoriteListMTF(FavoriteList):
    """List of element ordered with move to front heuristic"""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))  # delete return the element
    # override top because list is no longer sorted
    def top(self, k):

        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        # begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # find report and remove element with largest count
        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)


