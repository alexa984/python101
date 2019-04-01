def is_number_balanced(number):
    num_arr = to_digits(number)
    length = len(num_arr)
    skip_middle_index = 1 if length%2==1 else 0
    first_half = num_arr[0 : length//2]
    second_half = num_arr[length//2+skip_middle_index : length]
    if sum(first_half) == sum(second_half):
        return True
    return False