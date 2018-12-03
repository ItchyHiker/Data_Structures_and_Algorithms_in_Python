
def sumSquareLess(n):
    """return the sum of sqaure of all positive integers less than n"""
    return sum([x*x for x in range(1, n)])

if __name__ == "__main__":
    print(sumSquareLess(5))
