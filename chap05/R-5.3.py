import sys
def shrinkSize(n):
    data = [i for i in range(n)]
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; size in bytes:{1:4d}".format(a,b))
        data.pop()

if __name__ == "__main__":
    shrinkSize(30)

