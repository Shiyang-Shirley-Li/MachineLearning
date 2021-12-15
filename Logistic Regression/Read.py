"""
@author: Shirley (Shiyang) Li
Read data from a csv file path as two parts, the first is the
attributes values and the second is the label values
"""
import numpy as np


def read_data(path, num_features):
    x = []
    y = []
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')

            b = ['1'] #bias
            b.extend(terms)
            b = np.array(b[0:num_features+1]).astype(float)
            b = b.reshape(1, num_features+1)
            x.append(b)

            if terms[num_features] == '0':
                y.append(-1)
            else:
                y.append(1)

    return x, y