import re
def sum_of_numbers(input_string):
    numbers = re.findall('\d+', input_string)
    return sum([int(num) for num in numbers])
