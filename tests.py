import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_incorrect_string_value_is_not_price_value(self):
        self.assertIsNone(format_price(price='price'))

    def test_infinity_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price='Infinity'))

    def test_nan_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price='nan'))

    def test_bool_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price=True))
        self.assertIsNone(format_price(price=False))

    def test_list_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price=[]))
        self.assertIsNone(format_price(price=['1234']))

    def test_set_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price=set()))
        self.assertIsNone(format_price(price={1234}))

    def test_dict_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price={}))
        self.assertIsNone(format_price(price={'price': 1234}))

    def test_price_format_for_positive_integer_value(self):
        self.assertEqual('1 234', format_price(price='1234'))
        self.assertEqual('1 234', format_price(price='1234.0000'))
        self.assertEqual('1 234', format_price(price=1234))
        self.assertEqual('1 234', format_price(price=1234.0))

    def test_price_format_for_negative_integer_value(self):
        self.assertEqual('-4 321', format_price(price='-4321'))
        self.assertEqual('-4 321', format_price(price='-4321.0000'))
        self.assertEqual('-4 321', format_price(price=-4321))
        self.assertEqual('-4 321', format_price(price=-4321.0))

    def test_price_format_for_zero_value(self):
        self.assertEqual('0', format_price(price='0'))
        self.assertEqual('0', format_price(price='000.0000'))
        self.assertEqual('0', format_price(price=0))
        self.assertEqual('0', format_price(price=0.0))

    def test_price_format_for_positive_float_value(self):
        self.assertEqual('1 234.56', format_price(price='1234.56'))
        self.assertEqual('1 234.56', format_price(price=1234.56))

    def test_price_format_for_negative_float_value(self):
        self.assertEqual('-1 234.56', format_price(price='-1234.56'))
        self.assertEqual('-1 234.56', format_price(price=-1234.56))

    def test_price_format_for_million(self):
        self.assertEqual('1 234 567', format_price(price='1234567'))
        self.assertEqual('1 234 567.89', format_price(price=1234567.89))

    def test_price_format_for_billion(self):
        self.assertEqual('1 234 567 890', format_price(price='1234567890'))
        self.assertEqual('1 234 567 890.12', format_price(price=1234567890.12))

    def test_price_format_for_rounded_values(self):
        self.assertEqual('1 234.57', format_price(price=1234.567))
        self.assertEqual(
            '1 234.567',
            format_price(price='1234.567', count_digits_after_point=3),
        )
        self.assertEqual(
            '1 234.568',
            format_price(price=1234.5678, count_digits_after_point=3),
        )


if __name__ == '__main__':
    unittest.main()
