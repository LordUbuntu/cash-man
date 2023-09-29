import os
import platform
import pandas as pd
import datetime



# DATA
if platform.system() == "Linux":
    DATA_PATH = "{}/.local/share/cashman".format(os.path.expanduser('~'))
else:
    DATA_PATH = "{}/.cashman".format(os.path.expanduser('~'))
if not os.path.exists(DATA_PATH):
    print("'{}' doesn't exists, making path".format(DATA_PATH))
    os.makedirs(DATA_PATH)


# TODO: generalize data set and get queries, research dataframes more
def put(data: dict):
    # get file and path
    file = "{}.csv".format(data["Date"][0].year)
    path = "{}/{}".format(DATA_PATH, file)
    # create data_frame
    data_frame = pd.DataFrame(data)
    # add header if file exists, otherwise append data without header
    data_frame.to_csv(path,
                      mode='a',
                      index=False,
                      header=(not os.path.isfile(path)))


def get(mask=True, year=datetime.date().year):
    data_frame = pd.read_csv("{}/{}.csv".format(year, DATA_PATH, file))
    return data_frame.loc[mask]
