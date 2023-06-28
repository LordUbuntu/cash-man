# main cashman executable
import datetime
import click
import data


@click.group()
def cashman():
    pass


@cashman.command()
@click.option("--type",
              type=str,
              default="Unknown",
              help="what kind of transaction this was.")
@click.option("--date",
              type=click.DateTime(formats=['%Y-%m-%d']),
              default=str(datetime.date.today()),
              help="YYYY-MM-DD date transaction occured on.")
@click.option("--desc",
              type=str,
              default="Unknown",
              help="additional info about transaction")
@click.argument("amount", type=float)
def add(amount, type, date, desc):
    """Record a financial transaction.

    AMOUNT is the positive amount gained.
    """
    date = date.date()  # because click gives me timestamps I don't want
    data.store_dataframe({
        'Date': [date],
        'Type': [type],
        'Amount': [amount],
        'Description': [desc],
    })
    print("You recorded {} of type {} on date {}".format(amount, type, date))


@cashman.command()
@click.option("--type",
              type=str,
              default="Unknown",
              help="what kind of transaction this was.")
@click.option("--date",
              type=click.DateTime(formats=['%Y-%m-%d']),
              default=str(datetime.date.today()),
              help="YYYY-MM-DD date transaction occured on.")
@click.option("--desc",
              type=str,
              default="Unknown",
              help="additional info about transaction")
@click.argument("amount", type=float)
def sub(amount, type, date, desc):
    """Record a financial transaction.

    AMOUNT is the negative amount lost.
    """
    date = date.date()  # because click gives me timestamps I don't want
    data.store_dataframe({
        'Date': [date],
        'Type': [type],
        'Amount': [-amount],
        'Description': [desc],
    })
    print("You recorded {} of type {} on date {}".format(-amount, type, date))


# list transactions from date
@cashman.command()
@click.argument("date",
                type=click.DateTime(formats=['%Y-%m-%d']),
                default=str(datetime.date.today()))
def list(date):
    """List recent transactions.

    DATE is the YYYY-MM-DD date of transactions to list.
    """
    date = date.date()  # because click gives me timestamps I don't want
    data_frame = data.get_dataframe(date)
    if data_frame.empty:
        print("There were no transactions for {}".format(date))
    else:
        print("Your transactions for {} are: ".format(date))
        print(data_frame)


@cashman.command()
@click.argument("date",
                type=click.DateTime(formats=['%Y-%m-%d']),
                default=str(datetime.date.today()))
def net(date):
    """Calculates the net of transactions for a given date.
    
    DATE is the YYYY-MM-DD date of transactions to list.
    """
    date = date.date()  # because click gives me timestamps I don't want
    data_frame = data.get_dataframe(date)
    if data_frame.empty:
        print("There were no transactions for {}".format(date))
    else:
        total = data_frame["Amount"].sum()
        print("Your net transactions for {} are: {}".format(date, total))


# TODO: Rewrite read and write functions for dataframes to allow better
# filtering and selection
@cashman.command()
@click.argument("start",
                type=click.DateTime(formats=['%Y-%m-%d']),
                default=str(datetime.date.today()))
def diff(start, end):
    """Calculates the net change between two dates.

    DATE is the YYYY-MM-DD date of transactions to list.
    """
    start = start.date()
    end = end.date()



if __name__ == '__main__':
    cashman()
