class Category:
    def __init__(self, amount, for_what, _type, date):
        self.amount = amount
        self.for_what=for_what
        self._type = _type
        self.date = date

class Income(Category):
    def __init__(self, amount, for_what, date):
        super().__init__(amount, for_what, 'Income', date)

class Expense(Category):
    def __init__(self, amount, for_what, date):
        super().__init__(amount, for_what, 'Expense', date)