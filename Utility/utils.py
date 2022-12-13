# Utility function scripts
import os
from os import listdir
from os.path import isfile, join
import sys
import numpy as np
import pandas as pd
from icecream import ic


def read_metadata():
    local_path = r"Data/data/entities.csv"
    metadata = np.array(pd.read_csv(local_path))
    ic(metadata.shape)
    # Extract columns


def get_all_csv_names():
    local_path = r"Data/data/Magic Kingdom"
    csvs = os.listdir(local_path)
    ic(f"Number of csv files: {len(csvs)}")
    # ic(csvs)
    # Process names


if __name__ == '__main__':
    ic("Utility functions")
    # Get basic csv info
    get_all_csv_names()
    # Get metadata attraction info
    read_metadata()
