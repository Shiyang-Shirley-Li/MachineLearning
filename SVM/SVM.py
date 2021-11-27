"""
@author: Shirley (Shiyang) Li
Linear Regression by using batch gradient descent algorithm, stochastic gradient descent algorithm
and analytical form
"""
import numpy as np
import random
import Read
from scipy.optimize import minimize

C = 100 / 873
learning_rate = 0.25
weights = []
T = 100
x, y = Read.read_data("bank-note/train.csv", 5)
x_test, y_test = Read.read_data("bank-note/test.csv", 5)
initial_weight = np.zeros((5, 1))


# Primal
def SVM_primal_sgd(weight, ws):
    new_weight = weight
    shuffle_list = list(range(0, 872))  # 872 is the number of training data
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


def predict_result(weight, x, y):
    predict = 0
    if x.dot(weight) > 0:
        predict = 1
    else:
        predict = -1
    return y - predict


def run_primal_sgd():
    current_weight = initial_weight
    initial_LR = learning_rate
    for t in range(0, T):
        current_weight = SVM_primal_sgd(current_weight, weights)
        learning_rate = initial_LR / (1 + t * initial_LR / 2)  # Question 2a
        # learning_rate = initial_LR / (1 + t) # Question 2b

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


# Dual
data_x = np.concatenate(x)
data_y = np.array(y)
c_1 = np.where(np.prod(data_x, axis=1) > 0)
t = np.ones(872)
t[c_1] = -1
constraints = ({'type': 'eq', 'fun': lambda x: np.dot(x, t), 'jac': lambda x: t})
original_weight = np.ones((872, 1))
bound = [(0, C) for i in range(872)]


def loss_func(w):
    t_w = sum_axy(data_x, data_y, w)
    return 1 / 2 * np.dot(t_w, t_w.T) - w.sum()


def sum_axy(x, y, w):
    w = w.reshape(872, 1)
    N = x.shape[1]
    weight = np.zeros(N)
    w_1 = np.diag(w[:, 0])

    w_y = np.dot(w_1, y).reshape(872, 1)
    w_y_1 = np.diag(w_y[:, 0])

    wxy = np.dot(w_y_1, x)

    for i in range(0, 872):
        t_2 = axy[i, :].reshape(1, N)
        weight = np.add(weight, t_2)

    return weight


def run_dual():
    res = minimize(loss_func, original_weight, constraints=constraints, bounds=bound, method='SLSQP', options={}, tol=1e-6)
    weight_a = res.x

    weight_a = weight_a.reshape(872, 1)
    for i in range(0, 872):
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


if __name__ == '__main__':
    if sys.argv[1] == "primal":
        run_primal_sgd()
    elif sys.argv[1] == "dual":
        run_dual()
    elif sys.argv[1] == "kernal":
        run_kernal()
