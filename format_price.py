import argparse
import math


def format_price(price, count_digits_after_point=2):
    if isinstance(price, bool):
        return None

    try:
        price_float_value = float(price)
    except ValueError:
        return None

    if price_float_value is None:
        return None

    if not math.isfinite(price_float_value):
        return None

    if price_float_value.is_integer():
        return '{:,.0f}'.format(price_float_value).replace(',', ' ')
    else:
        return '{:,.{precision}f}'.format(
            price_float_value,
            precision=count_digits_after_point,
        ).replace(',', ' ')


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


if __name__ == '__main__':
    main()
