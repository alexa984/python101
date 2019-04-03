class Polynom:
    def __init__(self, expr):
        self.expr = expr
        signs = {'+', '-'}
        for symbol in expr:
            if symbol in signs:
                curr_monomial = expr[:symbol]
                if x in curr_monomial:
                    coeff = []
                    power = []
                    #take the position of x
                    pos = 0
                    for position, sym_monom in enumerate(curr_monomial):
                        if sym_monom == x:
                            pos = position

                    coeff = [:pos-1] #also remove *
                    try:
                        power = [pos+2:] #also remove ^
                    except:
                        power = 1 #if there is no symbols after x, the default power is 1

                        
                    #everything before x is coef, everything after is power
                

                expr = [symbol+1:]