def findMaximum(s, begin, end):
    """find the maximum element in sequence s using recursion"""
    debug = 0
    if begin ==  end:
        return s[begin]
    if begin == end - 1:
        return s[begin] if s[begin] >= s[end-1] else s[end-1]
    else:
        branch1 = findMaximum(s, begin, (end+begin)//2)
        branch2 = findMaximum(s, (begin+end)//2 + 1, end)
        if debug:
            print("branch1 max: ", branch1)
            print("branch2 max:", branch2)
        return branch1 if branch1 > branch2 else branch2
def findMaximum2(s,n):
    if n==1:
        return s[n-1]
    else:
        temp = findMaximum2(s, n-1)
        return s[n-1] if s[n-1] > temp else temp
if __name__ == "__main__":
    print(findMaximum([1,2,3], 0, 2))
    print(findMaximum([9,6], 0, 1))
    print(findMaximum([2,5,9,3,1,10,100], 0, 6))

    # method2
    print(findMaximum2([1,2,3], 3))
    print(findMaximum2([9,6], 2))
    print(findMaximum2([2,5,9,3,1,10,100], 7))


