def strToInt(str_digits):
    n = len(str_digits) - 1
    if n==0:
        return int(str_digits)
    else:
        return 10*strToInt(str_digits[0:n]) + int(str_digits[n])

if __name__ == "__main__":
    print(strToInt('1'))
    print(strToInt('13531'))

