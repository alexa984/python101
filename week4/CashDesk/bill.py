class Bill:
    def __init__(self, amount):
        if type(amount) is int:
            if amount > 0:
                self.amount = amount
            else:
                raise ValueError()
        else:
            raise TypeError()

    def __repr__(self):
        return 'A '+str(self.amount)+'$ bill'

    def __str__(self):
        return 'A '+str(self.amount)+'$ bill'

    def __int__(self):
        return self.amount

    def __hash__(self):
        return hash((self.amount, str(self.amount)))

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

