
def is_multiple(n, m):
    """if n = m*i, i is integer"""
    if n%m == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    for n in range(100):
        for m in range(1, 21):
            if is_multiple(n, m):
                print("{0:d} is multiple by {1:d}.".format(n, m))
            else:
                print("{0:d} is not multiple by {1:d}.".format(n, m))
