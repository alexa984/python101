import fractions
from functools import reduce

def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while True:
       if (z % x == 0) and (z % y == 0):
           lcm = z
           break
       z += 1

   return lcm

def collect_fractions(fracts):
    if not isinstance(fracts, list):
        raise fractions.ValidationError('You should provide list of fractions')
    else:
        nominators = []
        denominators = []
        for fract in fracts:
            simpl = fractions.simplify_fraction(fract)
            nominators.append(simpl[0])
            denominators.append(simpl[1])

        lcm_of_denominators = reduce(lambda x, y : lcm(x, y), denominators)
        for i in range(len(denominators)):
            nominators[i] *= lcm_of_denominators/denominators[i]
        
        denominators = [lcm_of_denominators]*(len(nominators))
        sum_of_fractions = (sum(nominators), lcm_of_denominators)

    return (fractions.simplify_fraction(sum_of_fractions))
