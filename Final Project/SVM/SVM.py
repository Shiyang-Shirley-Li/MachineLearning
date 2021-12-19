"""
@author: Shirley (Shiyang) Li
Linear Regression by using batch gradient descent algorithm, stochastic gradient descent algorithm
and analytical form
"""
import numpy as np
import random
import Read
from scipy.optimize import minimize
import sys

C = 100 / 873
learning_rate = 0.25
weights = []
T = 100
x, y = Read.read_data("../Data/train_final.csv", 14)
x_test, y_test = Read.read_data("../Data/test_final.csv", 14)
initial_weight = np.zeros((15, 1))


# SVM Primal SGD
def SVM_primal_sgd(weight, ws):
    new_weight = weight
    shuffle_list = list(range(0, 25000))
    random.shuffle(shuffle_list)

    for i in shuffle_list:
        weight_o = new_weight * (1 - learning_rate)
        temp = C * learning_rate * y[i] * x[i].reshape(5, 1)
        if y[i] * x[i].dot(new_weight) <= 1:
            new_weight = np.add(weight_o, temp)
        else:
            new_weight = weight_o
    ws.append(weight)
    return new_weight


def predict_result(weight, a, b):
    predict = 0
    if a.dot(weight) > 0:
        predict = 1
    else:
        predict = -1
    return b - predict


def run_primal_sgd():
    current_weight = initial_weight
    initial_LR = learning_rate
    for t in range(0, T):
        current_weight = SVM_primal_sgd(current_weight, weights)
        LR = initial_LR / (1 + t * initial_LR / 2)  # Question 2a
        # LR = initial_LR / (1 + t) # Question 2b

    last_weight = (weights[len(weights) - 1])
    # train error
    error_count = 0
    for i in range(0, len(y)):
        result = predict_result(last_weight, x[i], y[i])
        if result != 0:
            error_count += 1

    train_error = error_count / len(x)

    # test error
    error_num = 0
    for i in range(0, len(y_test)):
        result = predict_result(last_weight, x_test[i], y_test[i])
        if result != 0:
            error_num += 1

    test_error = error_num / len(x_test)

    print(C, "\n")
    print("Train error: ", train_error, "\n")
    print("Test error: ", test_error, "\n")


# SVM Dual
data_x = np.concatenate(x)
data_y = np.array(y)
c_1 = np.where(np.prod(data_x, axis=1) > 0)
t = np.ones(25000)
t[c_1] = -1
constraints = ({'type': 'eq', 'fun': lambda x: np.dot(x, t), 'jac': lambda x: t})
original_weight = np.ones((25000, 1))
bound = [(0, C) for i in range(25000)]


def loss_func(w):
    t_w = sum_axy(data_x, data_y, w)
    return 1 / 2 * np.dot(t_w, t_w.T) - w.sum()


def sum_axy(x, y, w):
    w = w.reshape(25000, 1)
    N = x.shape[1]
    weight = np.zeros(N)
    w_1 = np.diag(w[:, 0])

    w_y = np.dot(w_1, y).reshape(25000, 1)
    w_y_1 = np.diag(w_y[:, 0])

    wxy = np.dot(w_y_1, x)

    for i in range(0, 25000):
        t_2 = axy[i, :].reshape(1, N)
        weight = np.add(weight, t_2)

    return weight


def run_dual():
    res = minimize(loss_func, original_weight, constraints=constraints, bounds=bound, method='SLSQP', options={}, tol=1e-6)
    weight_a = res.x

    weight_a = weight_a.reshape(25000, 1)
    for i in range(0, 25000):
        temp = weight_a.item((i, 0))
        if temp > C:
            weight_a.itemset((i, 0), C)
        elif temp < 0:
            weight_a.itemset((i, 0), 0)
        else:
            weight_a.itemset((i, 0), temp)

    final_weight = sum_axy(data_x, data_y, weight_a)
    print(final_weight)

    final_weight = final_weight.reshape(5, 1)

    # train error
    error_count = 0
    for i in range(0, len(x)):
        result = predict_result(final_weight, x[i], y[i])
        if result != 0:
            error_count += 1

    train_error = error_count / len(x)

    # test error
    error_num = 0
    for i in range(0, len(x_test)):
        result = predict_result(final_weight, x_test[i], y_test[i])
        if result != 0:
            error_num += 1

    test_error = error_num / len(x_test)

    print(C, "\n")
    print("Weight and bias: ", final_weight.reshape(1, 5), "\n")
    print("Train error: ", train_error, "\n")
    print("Test error: ", test_error, "\n")


# SVM Kernel
kernel = lambda a, b: np.exp(-np.sum(np.square(a - b)) / learning_rate)


def gram(train, k):
    N = len(train)
    K = np.empty((N, N))
    for i in range(N):
        for j in range(N):
            K[i, j] = k(train[i], train[j])
    return K


kernel_data_x = gram(data_x, kernel)


def kernal_predict(w, a, b):
    n = len(x)
    new_x = np.empty((1, n))
    for i in range(n):
        new_x[0, i] = kernel(a, x[i])

    predict = 0
    if new_x.dot(w) > 0:
        predict = 1
    else:
        predict = -1

    return b - predict


def run_kernal():
    res = minimize(loss_func, original_weight, constraints=constraints, bounds=bound, method='SLSQP', options={},
                   tol=1e-6)
    weight_a = res.x

    weight_a = weight_a.reshape(25000, 1)
    for i in range(0, 25000):
        temp = weight_a.item((i, 0))
        if temp > C:
            weight_a.itemset((i, 0), C)
        elif temp < 0:
            weight_a.itemset((i, 0), 0)
        else:
            weight_a.itemset((i, 0), temp)

    final_weight = sum_axy(kernel_data_x, data_y, weight_a)
    final_weight = final_weight.reshape(25000, 1)
    # train error
    error_count = 0
    for i in range(0, len(x)):
        result = kernal_predict(final_weight,x[i], y[i])
        if result != 0:
            error_count += 1

    train_error = error_count / len(x)

    # test error
    error_num = 0
    for i in range(0, len(x_test)):
        result = kernal_predict(final_weight, x_test[i], y_test[i])
        if result != 0:
            error_num += 1

    test_error = error_num / len(x_test)

    print(C, "\n")
    print("Weight and bias: ", final_weight.reshape(1, 5), "\n")
    print("Train error: ", train_error, "\n")
    print("Test error: ", test_error, "\n")


if __name__ == '__main__':
    if sys.argv[1] == "primal":
        run_primal_sgd()
    elif sys.argv[1] == "dual":
        run_dual()
    elif sys.argv[1] == "kernal":
        run_kernal()