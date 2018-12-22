class SinglyLinkedList:
    """simple singly linked list"""
    class _Node:
        """nopublic class for storing singly linked node"""
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def get_next(self, node):
        """get the next node"""
        if self._head is None:
            raise ValueError("list is empty")
        if node == None:
            raise ValueError("node is should not be none")
        return node._next
    def get_element(self, node):
        """get the element at node"""
        return node._element
    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        new_node = self._Node(e, self._head)
        self._head = new_node
        if self._tail == None: # the first element in linked list
            self._tail = self._head
        self._size += 1

    def add_last(self, e):
        new_node = self._Node(e, None)
        if self._tail == None:
            self._head = self._tail = new_node
            self._tail._next = None
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def remove_first(self):
        """remove the first node in list and return the element in it"""
        if self._head is None:
            raise ValueError("list is empty!")
        e = self._head._element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e
def count_nodes(head):
    walk = head
    if walk._next is None:
        return 1
    else:
        return 1 + count_nodes(head._next)
if __name__ == "__main__":
    import random
    L = SinglyLinkedList()
    for i in range(10):
        L.add_last(random.randint(0, i))
    print(count_nodes(L._head))


