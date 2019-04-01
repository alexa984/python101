def to_digits(n):
    my_list = []
    while n > 0:
        my_list.insert(0, n%10)
        n = n//10
    return my_list
