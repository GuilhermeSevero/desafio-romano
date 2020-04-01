import unittest

from roman import to_roman


class TestDecimalToRoman(unittest.TestCase):

    def test_convert_to_I(self):
        self.assertEqual(to_roman(1), 'I', 'Convert To I')

    def test_convert_to_V(self):
        self.assertEqual(to_roman(5), 'V', 'Convert To V')

    def test_convert_to_X(self):
        self.assertEqual(to_roman(10), 'X', 'Convert To X')

    def test_convert_to_L(self):
        self.assertEqual(to_roman(50), 'L', 'Convert To L')

    def test_convert_to_C(self):
        self.assertEqual(to_roman(100), 'C', 'Convert To C')

    def test_convert_to_D(self):
        self.assertEqual(to_roman(500), 'D', 'Convert To D')

    def test_convert_to_M(self):
        self.assertEqual(to_roman(1000), 'M', 'Convert To M')


if __name__ == '__main__':
    unittest.main()
