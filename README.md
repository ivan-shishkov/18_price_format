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

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
