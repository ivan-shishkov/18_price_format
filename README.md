# Price Formatter

This script allows to get the pretty-formatted price representation (e.g. convert '1234567.89' to '1 234 567.89'). It can be used as:

* Standalone script with command line interface
* Module by using of direct call of the **format_price** function

# Quickstart

For script launch need to install Python 3.5.

## Usage as standalone script

Usage:

```bash

$ python3 format_price.py -h
usage: format_price.py [-h] [--digits DIGITS] price

positional arguments:
  price            a price for pretty formatting

optional arguments:
  -h, --help       show this help message and exit
  --digits DIGITS  a count of digits precision after decimal point for
                   rounding of price value if it is not a integer value
                   (default: 2)

```

Examples of script launch on Linux:

```bash

$ python3 format_price.py price12345
Could not to format price. Entered price is incorrect

$ python3 format_price.py 123456789
Pretty formatted price value: 123 456 789

$ python3 format_price.py 1234567.89
Pretty formatted price value: 1 234 567.89

$ python3 format_price.py 1234.567
Pretty formatted price value: 1 234.57

$ python3 format_price.py 1234.567 --digits 3
Pretty formatted price value: 1 234.567

```

## Usage as module

Module's interface is presented of the **format_price** function:

```py
format_price(price, count_digits_after_point=2)

```

Function arguments:

* **price** - a price for pretty formatting
* **count_digits_after_point** - a count of digits precision after decimal point for rounding of price value if it is not a integer value (default value is 2)

Function returns:

* **None** - when price value is incorrect and could not get the pretty-formatted price representation
* the pretty-formatted price representation otherwise

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
