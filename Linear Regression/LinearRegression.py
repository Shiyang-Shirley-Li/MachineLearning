"""
@author: Shirley (Shiyang) Li
Linear Regression by using batch gradient descent algorithm, stochastic gradient descent algorithm
and analytical form
"""
import numpy as np
from numpy import linalg as lin
import Read

algorithm_type = input("Enter the algorithm you'd like to use(bgd for batch gradient descent or sgd for stochastic "
                       "gradient descent or optimal for analytical form):")


# batch gradient descent algorithm
def compute_gradient(weights):
    gradient = float(0)
    hyp = train_data * np.transpose(weights)
    error = y_train - hyp
    gradient -= np.transpose(train_data) * error
    return gradient


def compute_cost(data, y, weights):
    sum_squared_error = float(0)
    num_examples = len(data)
    for i in range(num_examples):
        squared_error = np.square(y[i] - data[i] * np.transpose(weights))  # data??????
        sum_squared_error += squared_error
    return float(1 / 2 * sum_squared_error)


def batch_gradient_descent():
    learning_rate = 1

    while True:
        weights_pre = np.zeros(7)
        weights_pre = np.asmatrix(weights_pre)
        weights = np.zeros(7)
        weights = np.asmatrix(weights)
        cost_func_val = ""

        for t in range(73):
            # compute gradient
            gradient = compute_gradient(weights)
            # update w
            weights_pre = weights
            weights = weights_pre - learning_rate * np.transpose(gradient)

            cost_func_val += str(compute_cost(train_data, y_train, weights_pre)) + ","

            if lin.norm(weights - weights_pre) < 10E-6:
                return weights, learning_rate
        print(cost_func_val)
        learning_rate *= 0.5


# stochastic gradient descent algorithm
def stochastic_gradient_descent():
    learning_rate = 1

    while True:
        weights_pre = np.zeros(7)
        weights_pre = np.asmatrix(weights_pre)
        weights = np.zeros(7)
        weights = np.asmatrix(weights)
        cost_func_val = ""
        cost_pre = float('inf')
        cost = float(0)

        for t in range(73):
            # randomly sample a training example
            np.random.shuffle(train_full_data)
            random_data = train_full_data[:, :train_data.size // len(train_data)].reshape(train_data.shape)
            random_y = train_full_data[:, :y_train.size // len(y_train)].reshape(y_train.shape)

            for i in range(len(train_data)):
                cost_pre = cost
                weights_pre = weights
                for j in range(7):
                    hyp = random_data[i] * np.transpose(weights_pre)
                    error = random_y[i] - hyp
                    weights = weights_pre + learning_rate * error * random_data[i, j]

                cost = compute_cost(random_data, random_y, weights)
                cost_func_val += str(cost) + ","

            if np.abs(cost - cost_pre) < 10E-6:
                return weights, learning_rate

        print(cost_func_val)
        learning_rate *= 0.5


# Analytical form for calculating the optimal weight vector
def analytical_form_weight(data, y):
    data = np.transpose(data)
    return lin.pinv(data * np.transpose(data)) * data * y


if __name__ == '__main__':
    train_data = Read.read_data("concrete/train.csv", 53)[0]
    train_data = np.asmatrix(train_data)
    y_train = Read.read_data("concrete/train.csv", 53)[1]
    y_train = np.asmatrix(y_train)
    train_full_data = Read.read_data("concrete/train.csv", 53)[2]
    train_full_data = np.asmatrix(train_full_data)

    test_data = Read.read_data("concrete/test.csv", 50)[0]
    test_data = np.asmatrix(test_data)
    y_test = Read.read_data("concrete/test.csv", 50)[1]
    y_test = np.asmatrix(y_test)
    test_full_data = Read.read_data("concrete/test.csv", 50)[2]
    test_full_data = np.asmatrix(test_full_data)

    if algorithm_type == "bgd":
        batch_result = batch_gradient_descent()
        print("Weight: ", batch_result[0])
        print("Learning Rate: ", batch_result[1])
        print("Test Data Cost Function Value", compute_cost(test_data, y_test, batch_result[0]))
    elif algorithm_type == "sgd":
        stochastic_result = stochastic_gradient_descent()
        print("Weight: ", stochastic_result[0])
        print("Learning Rate: ", stochastic_result[1])
        print("Test Data Cost Function Value", compute_cost(test_data, y_test, stochastic_result[0]))
    elif algorithm_type == "optimal":
        print("Optimal weight for train data: ", analytical_form_weight(train_data, y_train))
