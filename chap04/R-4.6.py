def harmonicNumber(n):
    if n == 1:
        return 1;
    else:
        return 1/n + harmonicNumber(n-1)

if __name__ == "__main__":
    print(harmonicNumber(1))
    print(harmonicNumber(2))
    print(harmonicNumber(3))
