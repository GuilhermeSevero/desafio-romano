import unittest

from roman_numerals import roman_to_decimal


class TestRomanToDecimal(unittest.TestCase):

    def test_convert_to_1(self):
        self.assertEqual(roman_to_decimal('I'), 1, 'Convert To 1')

    def test_convert_to_5(self):
        self.assertEqual(roman_to_decimal('V'), 5, 'Convert To 5')

    def test_convert_to_10(self):
        self.assertEqual(roman_to_decimal('X'), 10, 'Convert To 10')

    def test_convert_to_50(self):
        self.assertEqual(roman_to_decimal('L'), 50, 'Convert To 50')

    def test_convert_to_100(self):
        self.assertEqual(roman_to_decimal('C'), 100, 'Convert To 100')

    def test_convert_to_500(self):
        self.assertEqual(roman_to_decimal('D'), 500, 'Convert To 500')

    def test_convert_to_1000(self):
        self.assertEqual(roman_to_decimal('M'), 1000, 'Convert To 1000')


if __name__ == '__main__':
    unittest.main()
