class Monome:

    def __init__(self, coeff = 1, power = 1):
        self.coeff = coeff
        self.power = power

    def clc_derivative(self):
        return Monomial(coeff=self.coeff*power, power-1)
