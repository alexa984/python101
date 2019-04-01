import fractions
def sort_fractions(fracts):
    simplified = [fractions.simplify_fraction(x) for x in fracts]
    answer = {}
    for i in range(0, len(fracts)):
        curr_fract = simplified[i]
        key = curr_fract[0]/curr_fract[1]
        print(key)
        answer[key] = fracts[i]
    for key in sorted(answer.keys()):
        print(answer[key])
        pass

sort_fractions([(2, 3),(1, 2),(5, 6),(26,8)])

#todo: don't use set, equal fracions are not showed, even 2/3 and 4/6 are reduced --> bug