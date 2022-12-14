import numpy as np
import pandas as pd
from icecream import ic
import datetime
import itertools
from itertools import filterfalse

# Custom import
from Utility.utils import get_all_csv_names

# Global constraints
OPEN, CLOSE = 9, 23


def get_info(name):
    pass


def refactor_cols(raw: np.ndarray):
    # Short version
    return np.concatenate([raw[:, 0:2], np.sum(raw[:, 2:4], axis=1, keepdims=True)], axis=1)

    # Verbose version
    # result = []
    # result.append(raw[:, 0:2])
    # ic(raw[:, 0:2].shape)
    # result.append(np.sum(raw[:, 2:4], axis=1, keepdims=True))
    # ic(np.sum(raw[:, 2:4], axis=1, keepdims=True).shape)
    # return np.concatenate(result, axis=1)


def preprocess(path, format='%Y-%m-%d %H:%M:%S'):
    df = pd.read_csv(path)
    # Check with NAs
    # Step 1: remove all rows where there are two NAs
    sactmin = np.array(df['SACTMIN'].notnull())
    spostmin = np.array(df['SPOSTMIN'].notnull())
    mask = np.logical_or(sactmin, spostmin)
    df = df[mask]
    # Step 2: fill with 0 (this is a trick)
    df = df.fillna(0)
    raw = np.array(df)
    # ic(raw.shape)
    # ic(raw[:, -1])
    # Re-combine last two columns
    raw = refactor_cols(raw)
    # ic(raw.shape)

    def condition(x):
        # Condition 1: Time not in OPEN -- CLOSE
        time_cond = int(datetime.datetime.strptime(x[1], format).hour) >= CLOSE or int(
            datetime.datetime.strptime(x[1], format).hour) < OPEN
        # Condition 2: Null: -999
        null_cond = x[-1] < 0
        return time_cond or null_cond
    return np.array(list(filterfalse(lambda x: condition(x), raw)))[:, 1:3]
    # data = np.array(list(filterfalse(lambda x: condition(x), raw)))
    # return data[:, 1:3]


def clean_all(dest):
    # TODO: (Xiaoyang) can save files with customized names if necessary
    raw, names = get_all_csv_names()
    # Clean each csv
    ic("Start cleaning data...")
    for idx, csv in enumerate(raw):
        ic(f"File {idx}: {csv} Cleaning...")
        local_path = "Data/data/Magic Kingdom/" + f"{csv}"
        data = preprocess(local_path)
        df = pd.DataFrame(data, columns=["Datetime", "Waiting Time"])
        df.to_csv(dest + f"{csv}")
        ic(f"File {idx}: {csv} Saved!")


if __name__ == "__main__":
    ic("Data Cleaning & Joining...")
    # Some examples
    # filename = "dumbo"
    filename = "7_dwarfs_train"
    filename = "princess_hall__rapunzel_tiana"
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
    data = preprocess(local_path, format)
    ic(data.shape)
    ic(data[0:5, :])

    # ACTUAL PROCESSING CODE (ABOVE ARE ALL EXAMPLES: can comment out if needed)
    # folder_name = "xysong_python"
    # destination = "Data/data/Magic Kingdom/" + f"{folder_name}/"
    # clean_all(destination)
