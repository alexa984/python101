import unittest
import collect_fractions
import fractions

class TestCollectFraction(unittest.TestCase):
    def test_when_two_fractions_with_same_lcm_are_added(self):
        test_data = [(2,3), (7, 3)]
        expected_output = (3, 1)
        self.assertEqual(collect_fractions.collect_fractions(test_data), expected_output)

    def test_when_list_with_tuple_with_zero_enumerator_is_calculated_then_return_exception(self):
        with self.assertRaises(ZeroDivisionError) as exc:
            collect_fractions.collect_fractions([(2,3), (7, 3), (1, 0)])

    def test_when_non_list_is_passed_then_return_validate_exception(self):
        with self.assertRaises(fractions.ValidationError) as exc:
            collect_fractions.collect_fractions({1, 6, 21.5})

if __name__ == '__main__':
    unittest.main()