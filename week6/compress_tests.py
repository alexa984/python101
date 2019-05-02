import unittest
from compress import compress
class TestMixins(unittest.TestCase):
    def test1_compress(self):
        result = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
        expected = ["Panda"]
        self.assertEqual(result, expected)

    def test2_compress(self):
        result = list(compress(["val1", "val2"], [False, False]))
        expected = []
        self.assertEqual(result, expected)

    def test3_compress(self):
        result = list(compress(["Panda"], [True]))
        expected = ["Panda"]
        self.assertEqual(result, expected)

    def test4_compress(self):
        result = list(compress([], []))
        expected = []
        self.assertEqual(result, expected)

if __name__ =='__main__':
    unittest.main()