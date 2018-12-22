from singly_linked_list import SinglyLinkedList
import random

def concatenate_lists(L, M):
    """concatenate s2 after s1"""
    new_list = SinglyLinkedList()
    if L._head == None:
        return M
    if M._head == None:
        return L
    l1 = len(L)
    l2 = len(M)
    head1 = L._head
    head2 = M._head
    while head1 != None:
        new_list.add_last(L.get_element(head1))
        head1 = head1._next

    while head2 != None:
        new_list.add_last(M.get_element(head2))
        head2 = head2._next
    return new_list

if __name__ == "__main__":

    L = SinglyLinkedList()
    M = SinglyLinkedList()
    for i in range(5):
        L.add_last(random.randint(0, i))
    for i in range(10):
        M.add_last(random.randint(0, i))
    print(len(L))
    print("elements in L:")
    walk = L._head
    while walk != None:
        print(L.get_element(walk))
        walk = walk._next

    print("elements in M:")
    walk = M._head
    while walk != None:
        print(M.get_element(walk))
        walk = walk._next

    print("elements in new list:")
    new_list = concatenate_lists(L, M)

    walk = new_list._head
    while walk != None:
        print(new_list.get_element(walk))
        walk = walk._next

