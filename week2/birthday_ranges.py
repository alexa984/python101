
def birthday_ranges(birthdays, ranges):
    result = []
    for my_range in ranges:
        result.append(len(list(x for x in birthdays if my_range[0] <= x <= my_range[1])))
    return result