# Utility function scripts
import os
from os import listdir
from os.path import isfile, join
import sys
import numpy as np
import pandas as pd
from icecream import ic
import itertools
from itertools import filterfalse


def read_metadata():
    local_path = r"Data/data/entities.csv"
    metadata = np.array(pd.read_csv(local_path))
    ic(metadata.shape)
    # Extract columns
    attractions = metadata[:, 1]
    # ic(attractions)
    return attractions


def get_all_csv_names():
    local_path = r"Data/data/Magic Kingdom"
    csvs = os.listdir(local_path)
    # ic(csvs[0][:-4])
    csvs = np.array(list(filterfalse(lambda x: x[-4:] != '.csv', csvs)))
    ic(type(csvs))
    ic(f"Number of csv files: {csvs.shape}")
    # ic(csvs)
    # Process names
    attractions = np.array([x[:-4] for x in csvs])
    # ic(attractions)
    return csvs, attractions


def find_num_matched(names, meta):
    # Deprecated!
    count = 0
    for item in names:
        if item in meta:
            count += 1
    ic(count)
    return count


if __name__ == '__main__':
    ic("Utility functions")
    # Get basic csv info
    raw, names = get_all_csv_names()
    # Get metadata attraction info
    meta_names = read_metadata()
    # ic(meta_names)
    ic(raw)
    # Find number of matched data
    # find_num_matched(names, meta_names)
