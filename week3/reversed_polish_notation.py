import math
def rpn_calculate(expression):
    items = []
    items = expression.split(' ')
    if len(items) < 2 :
        try:
            value = float(expression)
            return value
        except:
            Exception
            return None

    operators = ['+', '-', '*', '/', 'SQRT']
    i = 0
    while len(items) > 1 and i<len(items):
        item = items[i]
        if item in operators:
            if item != 'SQRT':
                it1 = items[i-2]
                it2 = items[i-1]
                expr = it1 + item + it2
                items[i] = str(eval(expr))
                items = items[:i-2] + items[i:]
                i-=2
            else:
                items[i] = str(math.sqrt(float(items[i-1])))
                items = items[:i-1] + items[i:]

        else:
            i+=1

    return float(items[0])

