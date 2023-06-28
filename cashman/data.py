import os
import pandas as pd
import datetime
# DATA
DATA_PATH = "{}/.local/share/cashman".format(os.path.expanduser('~'))
if not os.path.exists(DATA_PATH):
    print("'{}' doesn't exists, making path".format(DATA_PATH))
    os.makedirs(DATA_PATH)


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
def get_dataframe(mask, year=datetime.date().year):
    file = "{}.csv".format(year)
    path = "{}/{}".format(DATA_PATH, file)
    data_frame = pd.read_csv(path)
    return data_frame.loc[mask]
