import argparse
import math
import sys


def format_price(price, count_digits_after_point=2):
    if isinstance(price, bool):
        return None

    try:
        price_float_value = float(price)
    except (TypeError, ValueError):
        return None

    if not math.isfinite(price_float_value):
        return None

    if price_float_value.is_integer():
        price_formatted_string = '{:,.0f}'.format(price_float_value)
    else:
        price_formatted_string = '{:,.{precision}f}'.format(
            price_float_value,
            precision=count_digits_after_point,
        )

    return price_formatted_string.replace(',', ' ')


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

    pretty_formatted_price = format_price(
        price=price,
        count_digits_after_point=count_digits_after_point,
    )

    if pretty_formatted_price is None:
        sys.exit('Could not to format price. Entered price is incorrect')

    print('Pretty formatted price value: {}'.format(pretty_formatted_price))


if __name__ == '__main__':
    main()
