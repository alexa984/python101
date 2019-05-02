import unittest
from assert_raises import AssertRaises, Unexpected_type_exception, No_exception_occured, Unexpected_message

class TestAssertRaises(unittest.TestCase):
    def test_assert_raises_if_no_error_is_raised_inside(self):
        with self.assertRaises(No_exception_occured):
            with AssertRaises(ZeroDivisionError):
                x = 10/5

    def test_assert_raises_if_the_expected_error_is_raised(self):
        with AssertRaises(ZeroDivisionError):
            x = 5/0

    def test_assert_raises_if_unexpected_error_is_raised(self):
        with self.assertRaises(Unexpected_type_exception):
            with AssertRaises(TypeError):
                x = 5/0


if __name__ =='__main__':
    unittest.main()
