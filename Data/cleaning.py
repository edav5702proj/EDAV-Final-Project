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


def rename_cols(raw: np.ndarray):
    result = []
    result.append(raw[:, 0:2])
    # ic(raw[:, 0:2].shape)
    result.append(np.sum(raw[:, 2:4], axis=1, keepdims=True))
    # ic(np.sum(raw[:, 2:4], axis=1, keepdims=True).shape)
    return np.concatenate(result, axis=1)


def preprocess(path, format):
    df = pd.read_csv(path)
    # Check with NAs
    df = df.fillna(0)
    raw = np.array(df)
    ic(raw.shape)
    # ic(raw[:, -1])
    # Re-combine last two columns
    raw = rename_cols(raw)
    ic(raw.shape)

    def condition(x):
        # Time not in OPEN -- CLOSE
        time_cond = int(datetime.datetime.strptime(x[1], format).hour) >= CLOSE or int(
            datetime.datetime.strptime(x[1], format).hour) < OPEN
        # Null: -999
        null_cond = x[-1] < 0
        return time_cond or null_cond

    data = np.array(list(filterfalse(lambda x: condition(x), raw)))
    ic(data.shape)

    return data


if __name__ == "__main__":
    ic("Data Cleaning & Joining...")
    # Some examples
    # filename = "dumbo"
    filename = "7_dwarfs_train"
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
