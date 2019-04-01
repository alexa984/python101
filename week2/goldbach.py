import math
  
def find_primes(MAX): 
    primes = []
    marked = [False] * (int(MAX / 2) + 100); 
    for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1): 
        for j in range((i * (i + 1)) << 1, int(MAX / 2) + 1, 2 * i + 1): 
            marked[j] = True; 
  
    primes.append(2); 

    for i in range(1, int(MAX / 2) + 1): 
        if (marked[i] == False): 
            primes.append(2 * i + 1)
    return primes

def goldbach(n): 
    result = []
    primes = find_primes(n)
    i = 0
    while primes[i] <= n // 2: 
        temp = n - primes[i]
        if temp in primes: 
            result.append((primes[i], temp))
        i += 1
    return result
