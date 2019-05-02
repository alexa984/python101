from bill import Bill
class BatchBill:
    def __init__(self, bills):
        is_valid_input = all([isinstance(x, Bill) for x in bills])
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