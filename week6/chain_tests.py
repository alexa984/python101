import unittest
from chain import chain
class TestMixins(unittest.TestCase):
    def test_concatenate_two_ranges(self):
        result = list(chain(range(0, 4), range(4, 8)))
        expected = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, expected)

    def test_concatenate_two_tuples(self):
        result = tuple(chain( (0, 1, 2), (3, 4)))
        expected = (0, 1, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_concatenate_two_sets(self):
        result = set(chain({1, 2}, {3, 4, 5}))
        expected = {1, 2, 3, 4, 5}
        self.assertEqual(result, expected)


if __name__ =='__main__':
    unittest.main()