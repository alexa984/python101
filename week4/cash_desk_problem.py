from sortedcontainers import SortedSet

class Bill:
    def __init__(self, amount):
        if amount > 0:
            if type(amount) is int:
                self.amount = amount
            else:
                raise TypeError()
        else:
            raise ValueError()

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
        return self.amount<other.amount


class BatchBills:
    def __init__(self, bills):
        is_valid_input = all([type(x) is Bill for x in bills])
        if is_valid_input:
            self.bills = bills
        else:
            raise ValueError()

    def __len__(self):
        return len(self.bills)

    def total(self):
        total_bills = 0
        for bill in self.bills:
            total_bills += int(bill)

        return total_bills

    def __getitem__(self, index):
        return self.bills[index]

class CashDesk:
    def __init__(self):
        self.bills = []
        self.amount = 0

    def take_money(self, money):
        if type(money) is Bill:
            self.bills.append(money)
            self.amount+=int(money)

        elif type(money) is BatchBills:
            for bill in money:
                self.bills.append(bill)
                self.amount+=int(bill)

        else:
            raise ValueError()

    def total(self):
        return self.amount

    def inspect(self):
        for bill in SortedSet(self.bills):
            print (bill,'-', self.bills.count(bill))
