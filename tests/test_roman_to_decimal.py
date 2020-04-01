import unittest

from roman import to_decimal


class TestRomanToDecimal(unittest.TestCase):

    def test_convert_to_1(self):
        self.assertEqual(to_decimal('I'), 1, 'Convert To 1')

    def test_convert_to_5(self):
        self.assertEqual(to_decimal('V'), 5, 'Convert To 5')

    def test_convert_to_10(self):
        self.assertEqual(to_decimal('X'), 10, 'Convert To 10')

    def test_convert_to_50(self):
        self.assertEqual(to_decimal('L'), 50, 'Convert To 50')

    def test_convert_to_100(self):
        self.assertEqual(to_decimal('C'), 100, 'Convert To 100')

    def test_convert_to_500(self):
        self.assertEqual(to_decimal('D'), 500, 'Convert To 500')

    def test_convert_to_1000(self):
        self.assertEqual(to_decimal('M'), 1000, 'Convert To 1000')

    def test_convert_to_3(self):
        self.assertEqual(to_decimal('III'), 3, 'Convert To 2')

    def test_convert_to_9(self):
        self.assertEqual(to_decimal('IX'), 9, 'Convert To 9')

    def test_convert_to_14(self):
        self.assertEqual(to_decimal('XIV'), 14, 'Convert To 14')

    def test_convert_to_38(self):
        self.assertEqual(to_decimal('XXXVIII'), 38, 'Convert To 38')

    def test_convert_to_77(self):
        self.assertEqual(to_decimal('LXXVII'), 77, 'Convert To 77')

    def test_convert_to_92(self):
        self.assertEqual(to_decimal('XCII'), 92, 'Convert To 92')

    def test_convert_to_238(self):
        self.assertEqual(to_decimal('CCXXXVIII'), 238, 'Convert To 238')

    def test_convert_to_714(self):
        self.assertEqual(to_decimal('DCCXIV'), 714, 'Convert To 714')

    def test_convert_to_1198(self):
        self.assertEqual(to_decimal('MCXCVIII'), 1198, 'Convert To 1198')

    def test_convert_to_1240(self):
        self.assertEqual(to_decimal('MCCXL'), 1240, 'Convert To 1240')

    def test_convert_to_504(self):
        self.assertEqual(to_decimal('DIV'), 504, 'Convert To 504')

    def test_type_error_int(self):
        with self.assertRaises(TypeError):
            to_decimal(1)

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            to_decimal(['I', 'XIV'])


if __name__ == '__main__':
    unittest.main()
