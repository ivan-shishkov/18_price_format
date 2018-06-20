import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_incorrect_string_value_is_not_price_value(self):
        self.assertIsNone(format_price(price='price'))

    def test_infinity_is_incorrect_price_value(self):
        self.assertIsNone(format_price(price='Infinity'))

    def test_nan_is_incorrect_price_value_price(self):
        self.assertIsNone(format_price(price='nan'))


if __name__ == '__main__':
    unittest.main()
