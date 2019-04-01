def factorial(k):
    res = 1
    while k > 0:
        res *= k
        k = k-1
    return res

def fact_digits(n):
    result = 0
    while n > 0:
        x = n%10
        n = n//10
        result += factorial(x)
    return result