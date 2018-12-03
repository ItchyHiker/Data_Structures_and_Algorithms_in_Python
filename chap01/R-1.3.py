
def minmax(data):
    """return min max tuple of a sequence data."""
    temp = sorted(data)
    return temp[0], temp[-1]

if __name__ == "__main__":
    # use unpacking
    min_num, max_num = minmax([10, 9, -2, 5, 1 ])
    print(min_num)
    print(max_num)
