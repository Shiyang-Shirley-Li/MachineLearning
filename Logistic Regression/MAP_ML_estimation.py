import csv
import collections
import math
import copy
import numpy as np
import random
import Read
import sys

number_features = 4
T = 100
learning_rate = 0.0001

train_list, train_result_list = Read.read_data("bank-note/train.csv", 4)
train_num = 872
test_list, test_result_list = Read.read_data("bank-note/test.csv", 4)
initial_weight = np.zeros((5, 1))
output = []

# MAP ML SGD
def MAP_ML_sgd(weight, ws):
    # shuffle data
    next_weight = weight
    shuffle_list = list(range(0, train_num))
    random.shuffle(shuffle_list)

    for i in shuffle_list:
        r = learning_rate
        # update weight
        temp = r * (train_list[i] * (train_result_list[i] - train_list[i].dot(next_weight))).reshape(5, 1)
        if sys.argv[1] == "MAP":
            weight_o = next_weight * (1 - learning_rate / v)
            next_weight = np.add(temp, weight_o)
        else:
            next_weight = np.add(temp, weight)

    ws.append(weight)
    return next_weight


def predict_result(weight, a, b):
    predict = 0
    if a.dot(weight) > 0:
        predict = 1
    else:
        predict = -1
    return b - predict


def run_MAP_ML_estimation():
    current_weight = initial_weight
    original_LR = learning_rate
    for t in range(0, T):
        current_weight = MAP_ML_sgd(current_weight, output)
        # update learning rate
        r = original_LR / (1 + t * original_LR / 2)

    # run train data
    final_weight = (output[len(output) - 1])
    error_counter = 0
    for i in range(0, len(train_list)):
        result = predict_result(final_weight, train_list[i], train_result_list[i])
        if result != 0:
            error_counter = error_counter + 1

    error_train = error_counter / len(train_list)


    # run test data
    final_weight = (output[len(output) - 1])
    error_counter = 0
    for i in range(0, len(test_list)):
        result = predict_result(final_weight, test_list[i], test_result_list[i])
        if result != 0:
            error_counter = error_counter + 1

    error_test = error_counter / len(test_list)

    print("The train error = ", error_train)
    print("The test error = ", error_test)


if __name__ == '__main__':
    if sys.argv[1] == "MAP":
        v = 100
    run_MAP_ML_estimation()









