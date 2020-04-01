import unittest

from roman import to_roman


class TestDecimalToRoman(unittest.TestCase):

    def setUp(self) -> None:
        self.test_cases = (
            (1, 'I'),
            (3, 'III'),
            (4, 'IV'),
            (5, 'V'),
            (8, 'VIII'),
            (9, 'IX'),
            (10, 'X'),
            (38, 'XXXVIII'),
            (40, 'XL'),
            (50, 'L'),
            (77, 'LXXVII'),
            (100, 'C'),
            (138, 'CXXXVIII'),
            (170, 'CLXX'),
            (215, 'CCXV'),
            (238, 'CCXXXVIII'),
            (390, 'CCCXC'),
            (483, 'CDLXXXIII'),
            (500, 'D'),
            (1000, 'M'),
            (1198, 'MCXCVIII'),
            (1240, 'MCCXL'),
        )

    def test_decimal_to_roman(self):
        for decimal, roman in self.test_cases:
            self.assertEqual(to_roman(decimal), roman, f'{decimal} convert to {roman}')

    def test_type_error_int(self):
        with self.assertRaises(TypeError):
            to_roman('1')

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            to_roman([1, 92])
