import argparse
import math
import sys


def get_float_value(price):
    try:
        return float(price)
    except (TypeError, ValueError):
        return None


def get_price_string_format(price_float_value, count_digits_after_point):
    if price_float_value.is_integer():
        return '{:,.0f}'
    else:
        return '{:,.{precision}f}'.format(precision=count_digits_after_point)


def format_price(price, count_digits_after_point=2):
    if isinstance(price, bool):
        return None

    price_float_value = get_float_value(price)

    if price_float_value is None:
        return None

    if not math.isfinite(price_float_value):
        return None

    price_string_format = get_price_string_format(
        price_float_value=price_float_value,
        count_digits_after_point=count_digits_after_point,
    )

    return price_string_format.format(price_float_value).replace(',', ' ')


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'price',
        help='a price for pretty formatting',
        type=str,
    )
    parser.add_argument(
        '--digits',
        help='a count of digits precision after decimal point for rounding '
             'of price value if it is not a integer value (default: 2)',
        default=2,
        type=int,
    )
    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    price = command_line_arguments.price
    count_digits_after_point = command_line_arguments.digits

    if not price:
        sys.exit('Empty string entered')

    pretty_formatted_price = format_price(
        price=price,
        count_digits_after_point=count_digits_after_point,
    )

    if pretty_formatted_price is None:
        sys.exit('Could not to format price. Entered price is incorrect')

    print('Pretty formatted price value: {}'.format(pretty_formatted_price))


if __name__ == '__main__':
    main()
