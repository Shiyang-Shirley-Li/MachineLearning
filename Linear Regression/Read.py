import numpy as np


def read_data(path, num_examples):
    data = np.zeros((num_examples, 7))
    y = np.zeros((num_examples, 1))

    with open(path, 'r') as f:
        i = 0
        for line in f:
            terms = line.strip().split(',')
            data[i] = terms[0: 7]
            y[i] = terms[7]
            i += 1

    return data, y
