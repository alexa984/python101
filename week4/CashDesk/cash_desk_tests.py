import unittest
from cash_desk import CashDesk
from bill import Bill
from batch_bills import BatchBill

class TestCashDesk(unittest.TestCase):
    def test_create_cash_desk(self):
        desk = CashDesk()

    def test_take_money_from_one_bill(self):
        desk = CashDesk()
        test_bill = Bill(10)
        desk.take_money(test_bill)
        self.assertEqual(desk.bills, [test_bill])

    def test_take_money_from_bill_batch(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        self.assertEqual(desk.bills, bills)

    def test_take_money_when_no_bill_is_passed(self):
        desk = CashDesk()
        with self.assertRaises(ValueError):
            desk.take_money('no bill or batch')

    def test_desk_total(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]       
        batch = BatchBill(bills)        
        desk = CashDesk()       
        desk.take_money(batch)
        desk.take_money(Bill(10))       
        self.assertEqual(desk.total(), 390)

if __name__ =='__main__':
    unittest.main()