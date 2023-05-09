from datetime import datetime
from datetime import date
import argparse

def transaction_date(string):
    try:
        return datetime.strptime(string, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("not a valid date: {}".format(string))


parser = argparse.ArgumentParser(
        prog="cashman",
        description="record transactions on the cli",
        epilog="thank for checking out cashman!")

parser.add_argument("amount", type=float, help="+/- transaction amount")
parser.add_argument("--type", nargs='*', help="transaction category")
parser.add_argument("--date", type=transaction_date, default=str(date.today()), help="YYYY-MM-DD transaction date")

args = parser.parse_args()

if args.amount == 0:
    print("no transaction recorded")
else:
    print("recorded {} of type {} on date {}".format(args.amount, args.type, args.date))
