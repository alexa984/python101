import Monomial
class Polynomial:
    def __init__(self, variable, terms):
        self.terms = [] #list of objects of class monomial
        self.variable = variable

    def derive(self):
        result = ''
        for term in self.terms:
            der = str(term.calc_derivative()) #object type Monomial
            if der!='':
                result=result + der + '+'
        if result == '':
            result = '0'
        else:
            result = result[:-1] #remove the last +
        return result

    def parse_from_string(self, string):
        string.strip(' ') #remove all possible whitespaces between symbols
        terms = string.split('+')   #make list of all monomials as strings
        for term in terms:
            term_obj = Monomial.Monomial(0,self.variable, 0)
            term_obj.parse_from_string(term)
            self.terms.append(term_obj)





