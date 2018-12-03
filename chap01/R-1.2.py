
def is_even(k):
    if k%2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(100):
        if is_even(i):
            print("{0:d} is even.".format(i))
        else:
            print("{0:d} is not even.".format(i))
