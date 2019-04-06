class Monomial:
    def __init__(self, coefficient, variable, power):
        try:
            self.coefficient = int(coefficient)
            self.variable = str(variable)
            self.power = int(power)
        except:
            raise ValueError

    def __str__(self):
        result = ''
        if self.coefficient !=0:
            if self.power == 0:
                result = str(self.coefficient)
            elif self.power == 1:
                if self.coefficient!=1:
                    result = str(self.coefficient) +'*'+ self.variable
                else:
                    result = self.variable
            else:
                if self.coefficient!=1:
                    result = str(self.coefficient)+'*'+self.variable+'^'+str(self.power)
                else:
                    result = self.variable+'^'+str(self.power)
        else:
            result = ''
        return result

    def __repr__(self):
        return str(self)

    def __iter__(self):
        self.n = 0
        self.curr = 1
        return self

    def __next__(self):
        if self.n < self.curr:
            self.n += 1
            self.curr = 1
            return self.n
        else:
            raise StopIteration

    def calc_derivative(self):
        return Monomial(coefficient = self.coefficient*self.power,
            variable = self.variable,
            power = self.power -1)

    def parse_from_string(self, string):
        if self.variable in string:
            coeff, power = string.split(self.variable)
            coeff = coeff.strip('*')
            power = power.strip('^')
            if coeff == '':
                coeff = 1
            if power == '':
                power = 1
            self.coefficient = int(coeff)
            self.power = int(power)
        else:
            self.coeff = eval(string)
            self.power = 0
        return self

