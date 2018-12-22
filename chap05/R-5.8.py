"""
Experiment evaluate the efficiency of the pop method of Python's list
class when using varying indices as a parameter.
"""
import time

if __name__ == "__main__":
    N = [100, 1000, 10000, 100000, 1000000]
    for n in N:
        t_start = time.time()
        for t in range(100):
            x = [i for i in range(n)]
            x.pop(n//2)
        t_end = time.time()
        print("time for size {0} pop 1/2 :{1}".format(n, (t_end-t_start)/100))



