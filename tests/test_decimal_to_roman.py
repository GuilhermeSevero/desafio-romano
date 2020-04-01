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

    def test_convert_to_III(self):
        self.assertEqual(to_roman(3), 'III', 'Convert To III')

    def test_convert_to_IX(self):
        self.assertEqual(to_roman(9), 'IX', 'Convert To IX')

    def test_convert_to_XIV(self):
        self.assertEqual(to_roman(14), 'XIV', 'Convert To XIV')

    def test_convert_to_(self):
        self.assertEqual(to_roman(38), 'XXXVIII', 'Convert To XXXVIII')

    def test_convert_to_LXXVII(self):
        self.assertEqual(to_roman(77), 'LXXVII', 'Convert To LXXVII')

    def test_convert_to_XCII(self):
        self.assertEqual(to_roman(92), 'XCII', 'Convert To XCII')

    def test_convert_to_CCXXXVIII(self):
        self.assertEqual(to_roman(238), 'CCXXXVIII', 'Convert To CCXXXVIII')

    def test_convert_to_DCCXIV(self):
        self.assertEqual(to_roman(714), 'DCCXIV', 'Convert To DCCXIV')

    def test_convert_to_MCXCVIII(self):
        self.assertEqual(to_roman(1198), 'MCXCVIII', 'Convert To MCXCVIII')

    def test_convert_to_MCCXL(self):
        self.assertEqual(to_roman(1240), 'MCCXL', 'Convert To MCCXL')

    def test_convert_to_DIV(self):
        self.assertEqual(to_roman(504), 'DIV', 'Convert To DIV')

    def test_type_error_int(self):
        with self.assertRaises(TypeError):
            to_roman('1')

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            to_roman([1, 92])


if __name__ == '__main__':
    unittest.main()
