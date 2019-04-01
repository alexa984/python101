import math
class ValidationError(Exception):
    pass

def simplify_fraction(fraction):
    if not isinstance(fraction, tuple):
        raise ValidationError('You should provide tuple as a fraction')
    first_num = int(fraction[0])
    second_num = int(fraction[1])
    if second_num == 0:
        raise ZeroDivisionError('You can\'t divide by zero!')
    else:
        dividor = math.gcd(first_num, second_num)
        fraction = (first_num/dividor, second_num/dividor)
        return fraction
