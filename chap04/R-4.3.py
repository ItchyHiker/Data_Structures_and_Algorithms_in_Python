def power(x, n):
    """Compute the value x**n for integer n."""
    if n==0:
        return 1
    else:
        return x*power(x, n-1)
def power2(x, n):
    if n==0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial*partial
        if n%2 == 1:
            result *= x
        return result
if __name__ == "__main__":
    print(power(2, 5))
    print(power2(2, 5))


