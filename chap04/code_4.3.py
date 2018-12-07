import time
def binary_search(data, target, low, high):
    """Return True if target is found in indicated python of a Python list"""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

if __name__ == "__main__":
    seq = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
    for i in seq:
        t0 = time.time()
        binary_search(seq, i, 0, 15)
        t1 = time.time()
        print("total time:", t1-t0)
