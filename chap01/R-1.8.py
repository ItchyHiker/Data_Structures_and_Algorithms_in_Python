def equilent_index(i, n):
    """calculate the equilent index of i in length n string"""
    return n+i

if __name__ == "__main__":
    my_str = "Hello world!"
    for i in range(-len(my_str), -1):
        print(my_str[i], my_str[equilent_index(i, len(my_str))])


