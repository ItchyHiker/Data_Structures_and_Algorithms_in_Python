def reverse(S, start, end):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < end - 1:
        S[start], S[end-1] = S[end-1], S[start]
        reverse(S, start+1, end-1)


if __name__ == "__main__":
    S = [4,3,6,2,6]
    reverse(S, 0, 5)
    print(S)
