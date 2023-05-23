# main cashman executable
import os
import pandas as pd
import datetime
import click


@click.group()
def cashman():
    pass


@cashman.command()
@click.option("--type", type=str, default="Unknown", help="what kind of transaction this was.")
@click.option("--date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()), help="YYYY-MM-DD date transaction occured on.")
@click.argument("amount", type=float)
def add(amount, type, date):
    """Record a financial transaction.

    AMOUNT is the positive amount gained.
    """
    date = date.date()  # because click gives me timestamps I don't want
    store_dataframe({
        'Date': [date],
        'Type': [type],
        'Amount': [amount],
    })
    print("You recorded {} of type {} on date {}".format(amount, type, date))


@cashman.command()
@click.option("--type", type=str, default="Unknown", help="what kind of transaction this was.")
@click.option("--date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()), help="YYYY-MM-DD date transaction occured on.")
@click.argument("amount", type=float)
def sub(amount, type, date):
    """Record a financial transaction.

    AMOUNT is the negative amount lost.
    """
    date = date.date()  # because click gives me timestamps I don't want
    store_dataframe({
        'Date': [date],
        'Type': [type],
        'Amount': [-amount],
    })
    print("You recorded {} of type {} on date {}".format(-amount, type, date))


# list transactions from date
@cashman.command()
@click.argument("date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()))
def list(date):
    """List recent transactions.

    DATE is the YYYY-MM-DD date of transactions to list.
    """
    date = date.date()  # because click gives me timestamps I don't want
    print("Your transactions for {} are: ".format(date))
    print(get_dataframe(date))


@cashman.command()
@click.argument("date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()))
def net(date):
    """Calculates the net of transactions for a given date.
    
    DATE is the YYYY-MM-DD date of transactions to list.
    """
    date = date.date()  # because click gives me timestamps I don't want
    total = get_dataframe(date)["Amount"].sum()
    print("Your net transactions for {} are: {}".format(date, total))


def store_dataframe(data: dict):
    # TODO:
    # - Create standard data path
    # - Robust this

    # get file and path
    file = "{}.csv".format(datetime.date.today().year)
    path = "{}/{}".format(os.getcwd(), file)
    # create data_frame
    data_frame = pd.DataFrame(data)
    # add header if file exists, otherwise append data without header
    data_frame.to_csv(
            file,
            mode='a',
            index=False,
            header=(not os.path.isfile(path))
    )


def get_dataframe(date):
    file = "{}.csv".format(datetime.date.today().year)
    path = "{}/{}".format(os.getcwd(), file)
    data_frame = pd.read_csv(path)
    mask = (data_frame["Date"] == datetime.date.strftime(date, "%Y-%m-%d"))
    return data_frame.loc[mask]



if __name__ == '__main__':
    cashman()
