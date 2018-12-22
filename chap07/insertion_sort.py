from positional_list import PositionalList
import random
def insertion_sort(L):
    """sort PositionalList of comparable elements into nondecreasing order"""

    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

if __name__ == "__main__":
    L = PositionalList()
    for i in range(20):
        L.add_last(random.randint(1,i+5))

    for i in L:
        print(i)
    insertion_sort(L)
    print("After sort:")
    for i in L:
        print(i)

