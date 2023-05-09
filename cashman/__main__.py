# main cashman executable
from datetime import date
import click
# TODO might switch to argparse since I don't want users to have to put a -- at the end to record a negative transaction, though I might be able to get away with using a different subcommand for adding or subtracticing a transaction, though that seems painfully repetitive and overcomplicated.

@click.command()
@click.option("--type", default="Unknown", help="what kind of transaction this was.")
@click.option("--date", default=str(date.today()), help="YYYY-MM-DD date transaction occured on.")
@click.argument("amount")
def add(amount, type, date):
    """Record a financial transaction.

    AMOUNT is +/- the amount of the transaction in the record.
    """
    print("You recorded {} of type {} on date {}".format(amount, type, date))


def main():
    print("Hello, World! 你好世界！ Hola Mundo!")


if __name__ == '__main__':
    add()
