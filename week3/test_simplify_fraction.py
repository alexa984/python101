import fractions
import unittest

class TestFraction(unittest.TestCase):
    def test_when_prime_numbers_are_simplified_then_return_same(self):
        test_data = (3,17)
        expected_Result = (3, 17)
        self.assertEqual(fractions.simplify_fraction(test_data), expected_Result)
    
    def test_when_divider_is_zero(self):
        test_data = (6, 0)
        with self.assertRaises(ZeroDivisionError) as exc:
            fractions.simplify_fraction(test_data)

    def test_basic_case_when_simplify_fraction_then_divide_both_by_biggest_common_divisor(self):
        test_data = (21, 7)
        expected_result = (3, 1)
        self.assertEqual(fractions.simplify_fraction(test_data), expected_result)

    def test_if_validate_fraction_object_is_not_a_tuple(self):
        with self.assertRaises(fractions.ValidationError) as exc:
            fractions.simplify_fraction([5,5])

if __name__ == '__main__':
    unittest.main()