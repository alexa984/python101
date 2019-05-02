import unittest
from bill import Bill
from batch_bills import BatchBill

class TestBatchBill(unittest.TestCase):
    def test_create_batch(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)

    def test_create_batch_with_invalid_bill(self):
        with self.assertRaises(ValueError):
            bill1 = Bill(20)
            bill2 = "i am not a bill"
            batch = BatchBill([bill1, bill2])

    def test_batch_length(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        self.assertEqual(len(batch), 4)

    def test_batch_total(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        self.assertEqual(batch.total(), 180)

    def test_batch_get_item(self):
        b1 = Bill(20)
        b2 = Bill(50)
        batch = BatchBill([b1, b2])
        self.assertEqual(batch[1], b2)

if __name__ =='__main__':
    unittest.main()