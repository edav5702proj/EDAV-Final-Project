import numpy as np
import pandas as pd
from icecream import ic
import datetime
import itertools
from itertools import filterfalse

# Custom import
from Utility.utils import get_all_csv_names

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


def preprocess(path, format='%Y-%m-%d %H:%M:%S'):
    df = pd.read_csv(path)
    # Check with NAs
    df = df.fillna(0)
    raw = np.array(df)
    # ic(raw.shape)
    # ic(raw[:, -1])
    # Re-combine last two columns
    raw = rename_cols(raw)
    # ic(raw.shape)

    def condition(x):
        # Time not in OPEN -- CLOSE
        time_cond = int(datetime.datetime.strptime(x[1], format).hour) >= CLOSE or int(
            datetime.datetime.strptime(x[1], format).hour) < OPEN
        # Null: -999
        null_cond = x[-1] < 0
        return time_cond or null_cond

    data = np.array(list(filterfalse(lambda x: condition(x), raw)))
    # ic(data.shape)

    return data


def clean_all(dest):
    # TODO: (Xiaoyang) can save files with customized names
    raw, names = get_all_csv_names()
    # Clean each csv
    ic("Start cleaning data...")
    for idx, csv in enumerate(raw):
        ic(f"File {idx}: {csv} Cleaning...")
        local_path = "Data/data/Magic Kingdom/" + f"{csv}"
        data = preprocess(local_path)
        df = pd.DataFrame(data, columns=["Date", "Time", "Waiting Time"])
        df.to_csv(destination + f"{csv}")
        ic(f"File {idx}: {csv} Saved!")


if __name__ == "__main__":
    ic("Data Cleaning & Joining...")
    # Some examples
    # filename = "dumbo"
    # filename = "7_dwarfs_train"
    # local_path = "Data/data/Magic Kingdom/" + f"{filename}.csv"
    # # Convert to dataframe
    # df = pd.read_csv(local_path)
    # ic(df.head())

    # eg_date = df.head()['datetime'][0]
    # ic(eg_date)
    # format = '%Y-%m-%d %H:%M:%S'  # The format
    # datetime_str = datetime.datetime.strptime(eg_date, format)
    # ic(datetime_str.hour)

    # # Using preprocess function
    # data = preprocess(local_path, format)
    # ic(data.shape)

    # ACTUAL PROCESSING CODE (ABOVE ARE ALL EXAMPLES: can comment out if needed)
    folder_name = "xysong_python"
    destination = "Data/data/Magic Kingdom/" + f"{folder_name}/"
    clean_all(destination)
