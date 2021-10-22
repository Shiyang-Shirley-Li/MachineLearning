import numpy as np
from numpy import linalg as lin
import Read

algorithm = input()
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
        squared_error = np.square(y[i] - data[i] * np.transpose(weights))#data??????
        sum_squared_error += squared_error
    return float(1/2 * sum_squared_error)


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
    weights_pre = np.zeros(7)
    weights_pre = np.asmatrix(weights_pre)
    weights = np.zeros(7)
    weights = np.asmatrix(weights)


if __name__ == '__main__':
    train_data = Read.read_data("concrete/train.csv", 53)[0]
    train_data = np.asmatrix(train_data)
    y_train = Read.read_data("concrete/train.csv", 53)[1]
    y_train = np.asmatrix(y_train)

    test_data = Read.read_data("concrete/test.csv", 50)[0]
    test_data = np.asmatrix(test_data)
    y_test = Read.read_data("concrete/test.csv", 50)[1]
    y_test = np.asmatrix(y_test)

    batch_result = batch_gradient_descent()
    print("Weight: ", batch_result[0])
    print("Learning Rate: ", batch_result[1])
    print("Test Data Cost Function Value", compute_cost(test_data, y_test, batch_result[0]))
