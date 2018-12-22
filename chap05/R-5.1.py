import sys
data = []
n = 30
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; size in bytes:{1:4d}".format(a,b))
    data.append(None)


