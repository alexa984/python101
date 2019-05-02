import unittest
from bill import Bill
class TestBill(unittest.TestCase):
    def test_create_bill(self):
        a = Bill(100)

    def test_create_bill_with_negative_amount_of_money(self):
        with self.assertRaises(ValueError):
            a = Bill(-10)

    def test_create_bill_with_floating_point_number_amount(self):
        with self.assertRaises(TypeError):
            a = Bill(21.5)

    def test_create_bill_with_something_other_than_number(self):
        with self.assertRaises(TypeError):
            a = Bill("not a number")

    def test_int_bill(self):
        a = Bill(10)
        self.assertEqual(int(a), 10)

    def test_bill_str(self):
        a = Bill(10)
        self.assertEqual(str(a), 'A 10$ bill')

    def test_bill_eq_if_equal(self):
        a = Bill(10)
        b = Bill(10)
        self.assertEqual(a, b)

    def test_bill_eq_if_not_equal(self):
        a = Bill(10)
        b = Bill(5)
        self.assertNotEqual(a, b)

    def test_bill_lt_if_true(self):
        a = Bill(10)
        b = Bill(5)
        self.assertTrue(b < a)

    def test_bill_lt_if_not_true(self):
        a = Bill(10)
        b = Bill(5)
        self.assertFalse(a < b)


if __name__ =='__main__':
    unittest.main()