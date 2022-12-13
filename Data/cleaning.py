import numpy as np
import pandas as pd
from icecream import ic
import datetime
import itertools
from itertools import filterfalse

# Gloabl constraints
OPEN, CLOSE = 9, 23


def get_info(name):
    pass


def preprocess(path, format):
    raw = np.array(pd.read_csv(path))
    ic(raw.shape)
    # ic(raw[0][1])
    data = np.array(list(filterfalse(
        lambda x: int(datetime.datetime.strptime(x[1], format).hour) > CLOSE
        or int(datetime.datetime.strptime(x[1], format).hour) < OPEN, raw)))
    ic(data.shape)
    return data


if __name__ == "__main__":
    ic("Data Cleaning & Joining...")
    # Some examples
    # filename = "dumbo"
    # filename = "7_dwarfs_train"
    filename = ""
    local_path = "Data/data/Magic Kingdom/" + f"{filename}.csv"
    # Convert to dataframe
    df = pd.read_csv(local_path)
    ic(df.head())

    eg_date = df.head()['datetime'][0]
    ic(eg_date)
    format = '%Y-%m-%d %H:%M:%S'  # The format
    datetime_str = datetime.datetime.strptime(eg_date, format)
    ic(datetime_str.hour)

    # Using preprocess function
    preprocess(local_path, format)
