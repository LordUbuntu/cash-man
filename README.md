# Cash Man

A personal financial expenses tracker command line tool written in Python 3.

## Info

The program is built using Rich, Fire (or Click), and using CSV to read and store information for portability.

## Usage

`cashman add <amount> <type> <date>`

where `<amount>` is the amount of money expended, `<type>` is the "category" of the expense, such as "food" or "travel", and `<date>` is an optional `YYYY-MM-DD` format specifier if the expense was not on the current date. Ommitting `<date>` will assume the current date.
