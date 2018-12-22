from double_linkedbase import _DoublyLinkedBase
class PositionalList(_DoublyLinkedBase):
    """A sequential container allowing positional access"""

    # nested class
    class Position:
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    #-----------utility methods--------------#
    def _validate(self, p):
        """return position's node or raise approriate error is invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None: # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self,node):
        """return positional instance for given node"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    #-------------accessor------------------#
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """return the position before Position p"""
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        """generate a forward iteration of the elements in the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #-----------------mutators---------------#
    def _insert_between(self, e, predecessor, successor):
        """add elements between ecisting nodes and return new position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    def add_first(self, e):
        """insert element at the front of the list and return new position"""
        return self._insert_between(e, self._header, self._header._next)
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    def delete(self, p):
        """remove and return element at position p"""
        original = self._validate(p)
        return self._delete_node(original)
    def replace(self, p, e):
        """replace the element at position p with element e"""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

