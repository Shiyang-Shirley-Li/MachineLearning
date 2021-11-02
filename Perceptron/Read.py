"""
@author: Shirley (Shiyang) Li
Read data from a csv file path as two parts, the first is the
attributes values and the second is the label values
"""
import numpy as np


def read_data(path, num_examples):
    data = np.zeros((num_examples, 4))
    y = np.zeros((num_examples, 1))  # for matrix format use

    with open(path, 'r') as f:
        i = 0
        for line in f:
            terms = line.strip().split(',')
            data[i] = terms[0: 4]
            if terms[4] == '0':
                y[i] = -1
            else:
                y[i] = terms[4]
            i += 1

    return data, y
