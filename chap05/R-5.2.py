import sys
def changeIndexs(n):
    data = []
    indexs = []
    curMem = 0
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; size in bytes:{1:4d}".format(a,b))
        if b > curMem:
            indexs.append(k)
            curMem = b
        data.append(None)

    return indexs

if __name__ == "__main__":
    seq = changeIndexs(50)
    print(seq)


