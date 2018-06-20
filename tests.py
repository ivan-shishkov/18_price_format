import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_incorrect_string_value_is_not_price_value(self):
        self.assertIsNone(format_price(price='price'))


if __name__ == '__main__':
    unittest.main()
