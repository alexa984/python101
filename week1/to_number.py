def join(items): #expects string
    result = ''
    for item in items:
        result = result + item
    return result

def to_number(digits):
    chars = [str(digit) for digit in digits]
    return int(join(chars))
