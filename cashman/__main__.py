# main cashman executable
import os
import pandas as pd
from datetime import date
import click


@click.group()
def cashman():
    pass


@cashman.command()
@click.option("--type", type=str, default="Unknown", help="what kind of transaction this was.")
@click.option("--date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(date.today()), help="YYYY-MM-DD date transaction occured on.")
@click.argument("amount", type=float)
def add(amount, type, date):
    """Record a financial transaction.

    AMOUNT is the positive amount gained.
    """
    df = pd.DataFrame({
        'Date': [date],
        'Type': [type],
        'Amount': [amount],
    })
    add_data(df)
    print("You recorded {} of type {} on date {}".format(amount, type, date))


@cashman.command()
@click.option("--type", type=str, default="Unknown", help="what kind of transaction this was.")
@click.option("--date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(date.today()), help="YYYY-MM-DD date transaction occured on.")
@click.argument("amount", type=float)
def sub(amount, type, date):
    """Record a financial transaction.

    AMOUNT is the negative amount lost.
    """
    print("You recorded {} of type {} on date {}".format(-amount, type, date))


# list transactions from date
@cashman.command()
@click.argument("date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(date.today()))
def list(date):
    """List recent transactions.

    DATE is the YYYY-MM-DD date of transactions to list.
    """
    print("Your transactions for {} are: []".format(date))


def add_data(data_frame):
    # TODO:
    # - Create standard data path
    # - Check existence of csv to ensure headers are there
    # - Ensure add and sub functions use this one
    # - Robust this
    data_frame.to_csv('{}.csv'.format(date.today().year), mode='a', header=False)



if __name__ == '__main__':
    cashman()
