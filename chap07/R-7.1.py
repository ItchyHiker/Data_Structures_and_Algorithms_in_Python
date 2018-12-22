from linked_stack import LinkedStack
import random

def find_second_to_last_node(s):
    if len(s) == 1:
        raise ValueError("s only has one element!")
    head1 = s._head
    head2 = head1._next
    while head2._next != None:
        head1 = head2
        head2 = head2._next
    return head1

if __name__ == "__main__":

    s = LinkedStack()
    for i in range(10):
        s.push(random.randint(i, 20))
    head = s._head
    for i in range(10):
        print(head._element)
        head = head._next
    node = find_second_to_last_node(s)
    print("second to last element of s is:", node._element)
