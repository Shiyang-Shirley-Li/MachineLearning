"""
@author: Shirley (Shiyang) Li
Read data from a csv file path as two parts, the first is the
attributes values and the second is the label values
"""
import numpy as np


def read_data(path, num_examples):
    full_data = np.zeros((num_examples, 8))
    data = np.zeros((num_examples, 7))
    y = np.zeros((num_examples, 1))  # for matrix format use

    with open(path, 'r') as f:
        i = 0
        for line in f:
            terms = line.strip().split(',')
            full_data[i] = terms
            data[i] = terms[0: 7]
            y[i] = terms[7]
            i += 1

    return data, y, full_data
