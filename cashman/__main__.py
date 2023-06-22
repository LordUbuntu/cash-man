# main cashman executable
from datetime import date
import click
<<<<<<< Updated upstream
# TODO might switch to argparse since I don't want users to have to put a -- at the end to record a negative transaction, though I might be able to get away with using a different subcommand for adding or subtracticing a transaction, though that seems painfully repetitive and overcomplicated.
=======


DATA_PATH = "{}/.local/share/cashman".format(os.path.expanduser('~'))
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

>>>>>>> Stashed changes




def store_dataframe(data: dict):
    # get file and path
    file = "{}.csv".format(data["Date"][0].year)
    path = "{}/{}".format(DATA_PATH, file)
    # create data_frame
    data_frame = pd.DataFrame(data)
    # add header if file exists, otherwise append data without header
    data_frame.to_csv(
            path,
            mode='a',
            index=False,
            header=(not os.path.isfile(path))
    )


# TODO: filter out dataframes
def get_dataframe(mask, year=date.year):
    file = "{}.csv".format(year)
    path = "{}/{}".format(DATA_PATH, file)
    data_frame = pd.read_csv(path)
    return data_frame.loc[mask]





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
<<<<<<< Updated upstream
    print("Your transactions for {} are: []".format(date))


def main():
    print("Hello, World! 你好世界！ Hola Mundo!")
=======
    date = date.date()  # because click gives me timestamps I don't want
    data_frame = get_dataframe(date)
    if data_frame.empty:
        print("There were no transactions for {}".format(date))
    else:
        print("Your transactions for {} are: ".format(date))
        print(data_frame)


@cashman.command()
@click.argument("date", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()))
def net(date):
    """Calculates the net of transactions for a given date.
    
    DATE is the YYYY-MM-DD date of transactions to list.
    """
    date = date.date()  # because click gives me timestamps I don't want
    data_frame = get_dataframe(date)
    if data_frame.empty:
        print("There were no transactions for {}".format(date))
    else:
        total = data_frame["Amount"].sum()
        print("Your net transactions for {} are: {}".format(date, total))


# TODO: Rewrite read and write functions for dataframes to allow better
# filtering and selection
@cashman.command()
@click.argument("start", type=click.DateTime(formats=['%Y-%m-%d']), default=str(datetime.date.today()))
def diff(start, end):
    """Calculates the net change between two dates.

    DATE is the YYYY-MM-DD date of transactions to list.
    """
    start = start.date()
    end = end.date()




>>>>>>> Stashed changes


if __name__ == '__main__':
    cashman()
