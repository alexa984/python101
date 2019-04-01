import unittest
from reversed_polish_notation import rpn_calculate

class TestReversedPolishNotation(unittest.TestCase):
    def test_when_two_numbers_are_passed_with_plus_afterwards_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_only_one_number_is_passed_then_return_the_same_digit(self):
        expr = '45'
        self.assertEqual(rpn_calculate(expr), 45)

    def test_sqrt_of_one_number(self):
        expr = '9 SQRT'
        self.assertEqual(rpn_calculate(expr), 3)

    def test_when_sqrt_of_an_expression_is_passed_then_return_only_one_number(self):
        expr = '1 2 3 5 + + * 10 * SQRT'
        self.assertEqual(rpn_calculate(expr), 10)

    def test_when_two_numbers_are_passed_with_asterisk_then_return_sum_of_them(self):
        expr = '5 6 *'
        self.assertEqual(rpn_calculate(expr), 30)

    def test_when_two_numbers_are_passed_with_division_sign_between_then_return_result_of_division(self):
        expr = '8 2 /'
        self.assertEqual(rpn_calculate(expr), 4)

    def test_if_only_operator_is_passed_then_return_none(self):
        expr = 'SQRT'
        self.assertEqual(rpn_calculate(expr), None)

    def test_if_only_one_non_valid_operand_is_passed(self):
        expr = 'alabala'
        self.assertEqual(rpn_calculate(expr), None)

if __name__ == '__main__':
    unittest.main()