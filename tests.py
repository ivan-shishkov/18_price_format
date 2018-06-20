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


if __name__ == '__main__':
    unittest.main()
