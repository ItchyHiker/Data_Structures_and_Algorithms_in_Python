"""
Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclu- sive, with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated.
"""
import random

def sample(n=2):
    """produce sample sequence for testing.
    n: the length of the sequence
    """

    assert n >= 2
    l = []
    for i in range(1, n):
        l.append(i)
    l.append(random.choice(l))
    randum.shuffle(l)
    return l

def find1(l):
    """using nlogn sort function"""
    l.sort # O(nlogn)
    last=None
    for i in l: # O(n) loop
        if i == last:
            return last
        last = i

def find2(l):
    """using the trick of sum function"""
    n = len(l) # O(1)
    return sum(l) - (n*n - n)/2  # O(n) for sum

