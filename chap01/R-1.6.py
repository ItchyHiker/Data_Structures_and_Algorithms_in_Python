
def oddPositiveSumSquare(n):
    """return the sum of squares of all the odd positive integers less than n"""
    if not isinstance(n, (int)):
        raise TypeError("x must be integer.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if n == 1:
        return 1
    else:
        return sum([x*x for x in range(1, n) if x%2])

if __name__ == "__main__":
    print(oddPositiveSumSquare(5))
    print(oddPositiveSumSquare(1))
#    print(oddPositiveSumSquare(-1))
    print(oddPositiveSumSquare(1.1))
