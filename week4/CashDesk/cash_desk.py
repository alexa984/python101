from sortedcontainers import SortedSet
from batch_bills import BatchBill
from bill import Bill
class CashDesk:
    def __init__(self):
        self.bills = []
        self.amount = 0

    def take_money(self, money):
        if type(money) is Bill:
            self.bills.append(money)
            self.amount+=int(money)

        elif isinstance(money, BatchBill):
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
