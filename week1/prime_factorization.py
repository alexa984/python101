def prime_factor(number):
    n = number
    factors = []
    result = []
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n = n//i
    
    if len(factors) > 0:
        for val in range(2, factors[-1]+1):
            if val in factors:
                result.append((val, factors.count(val)))
    else:
        #if number is prime
        result.append((number, 1))

    return result
