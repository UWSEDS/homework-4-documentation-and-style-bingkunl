'''
read data from url and
input them into pandas dataframe and
run some test
'''
import pandas as pd
import numpy as np


def create_dataframe(url):
    '''create pandas dataframe using url'''
    data = pd.read_csv(url)
    # return data in pandas dataframe
    return data


def test_create_dataframe(data, names):
    '''test if dataframe satisfy creation requirement '''
    for name in data:
        length = len(data[name])
        # check if data attributes satisfy requirement
        if name not in names:
            return False
        # check if there are at least ten rows
        if length < 10:
            return False
        # check if each column have same value type
        for i in range(length-1):
            t_1 = type(data[name][i])
            t_2 = type(data[name][i+1])
            if t_1 != t_2:
                return False
    # return true if satisfy all requirements
    return True


def check_value_type(data):
    '''check if all values are correct'''
    for name in data:
        length = len(data)
        # check if each column have same value type
        for i in range(length-1):
            t_1 = type(data[name][i])
            t_2 = type(data[name][i+1])
            if t_1 != t_2:
                return False
    # return true if all values are correct
    return True


def check_nan_value(data):
    '''check if there is nan value'''
    for name in data:
        length = len(data)
        for i in range(length):
            value = data[name][i]
            # return false if find nan
            if value is np.nan:
                return False
    # return true if there is no nan
    return True


def verify_num_of_rows(data):
    '''check if there is at least one row'''
    return bool(data)
