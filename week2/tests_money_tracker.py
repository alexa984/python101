import money_tracker
import unittest

class TestMoneyTracker(unittest.TestCase):
    def test_show_user_incomes(self):
        all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        testing = money_tracker.show_user_incomes(all_user_data)
        self.assertEqual(testing, [(10, 'Deposit'), (50, 'Savings'), (700, 'Salary')])

    def test_list_expense_categories(self):
        all_user_data = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_output = [(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'), (12, 'Eating Out'), (15, 'Food'), (41.79, 'Food'), (7, 'House'), (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')]
        self.assertEqual(money_tracker.list_user_expenses_ordered_by_categories(all_user_data), expected_output)

    def test_show_user_data_per_date(self):
        date = '23-03-2019'
        all_user_data = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_output = [(50, 'Savings', 'New Income'), (15, 'Food', 'New Expense'), (200, 'Deposit', 'New Income'), (5, 'Sports', 'New Expense'), (10, 'Deposit', 'New income')]
        self.assertEqual(money_tracker.show_user_data_per_date(date, all_user_data), expected_output)

    def test_list_income_categories(self):
        all_user_data = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_output = ['Deposit', 'Salary', 'Savings']
        result = money_tracker.list_income_categories(all_user_data)
        self.assertEqual(result.sort(), expected_output.sort()) #because order doesn't matter

if __name__ == '__main__':
    unittest.main()