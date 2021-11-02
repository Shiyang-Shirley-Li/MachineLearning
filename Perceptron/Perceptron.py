import Read
import numpy as np
# Variables
T = 10


# Standard Perceptron Algorithm
def standard_perceptron(learning_rate=1.0):
    weight = np.zeros((1, 4), dtype="float")
    weight = np.asmatrix(weight)

    for epoch in range(T):
        random_x, random_y = shuffle_data(train_data[0], train_data[1])
        for i in range(len(train_data[1])):
            example_x = np.asmatrix(random_x[i])
            example_y = np.asmatrix(random_y[i])

            prediction = np.sign(example_x * (np.transpose(weight)))
            if prediction != example_y:
                weight = weight + learning_rate * example_y * example_x

        train_data_matrix = np.asmatrix(train_data[0])
        train_predictions = np.sign(weight*np.transpose(train_data_matrix))
        train_error = calculate_error(train_predictions, train_data[1])

        test_data_matrix = np.asmatrix(test_data[0])
        test_predictions = np.sign(weight*np.transpose(test_data_matrix))
        test_error = calculate_error(test_predictions, test_data[1])

        print(epoch, " Train error: ", train_error, " Test error: ", test_error)
    
    print("Weight vector: ", weight)


def shuffle_data(attribute_data, label_data):
    full_data = np.c_[attribute_data.reshape(len(attribute_data), -1), label_data.reshape(len(label_data), -1)]
    np.random.shuffle(full_data)
    random_data = full_data[:, :attribute_data.size // len(attribute_data)].reshape(attribute_data.shape)
    random_label = full_data[:, attribute_data.size // len(attribute_data)].reshape(label_data.shape)
    return random_data, random_label


def calculate_error(predictions, label_data):
    label_data = np.asmatrix(label_data)
    return np.count_nonzero(np.multiply(np.transpose(label_data), predictions) == -1)/len(label_data)


# Voted Perceptron Algorithm
def voted_perceptron(learning_rate=1.0):
    weight = np.zeros((1, 4), dtype="float")
    weight = np.asmatrix(weight)
    weights = []
    weights.append(weight)
    m = 0
    votes = [0]

    for epoch in range(T):
        for i in range(len(train_data[1])):
            example_x = np.asmatrix(train_data[0][i])
            example_y = np.asmatrix(train_data[1][i])

            prediction = np.sign(example_x * (np.transpose(weight)))
            if prediction != example_y:
                weight = weight + learning_rate * example_y * example_x
                weights.append(weight)
                votes.append(1)
                m += 1
            else:
                votes[m] += 1

        train_data_matrix = np.asmatrix(train_data[0])
        train_predictions = calculate_voted_predictions(weights, votes, train_data_matrix, len(train_data[1]))
        train_error = calculate_error(train_predictions, train_data[1])

        test_data_matrix = np.asmatrix(test_data[0])
        test_predictions = calculate_voted_predictions(weights, votes, test_data_matrix, len(test_data[1]))
        test_error = calculate_error(test_predictions, test_data[1])

        print(epoch, " Train error: ", train_error, " Test error: ", test_error)
    
    print("Votes: ", votes)
    print("Weights vector: ", weights)


def calculate_voted_predictions(weights, votes, data_matrix, data_len):
    predictions = np.zeros((1, data_len))
    for i in range(len(votes)):
        prediction = np.sign(weights[i] * np.transpose(data_matrix))
        predictions += votes[i] * prediction
    return np.sign(predictions)


# Average Perceptron Algorithm
def average_perceptron(learning_rate=1.0):
    weight = np.zeros((1, 4), dtype="float")
    weight = np.asmatrix(weight)
    average = weight.copy()

    for epoch in range(T):
        for i in range(len(train_data[1])):
            example_x = np.asmatrix(train_data[0][i])
            example_y = np.asmatrix(train_data[1][i])

            prediction = np.sign(example_x * (np.transpose(weight)))
            if prediction != example_y:
                weight = weight + learning_rate * example_y * example_x
            average += weight

        train_data_matrix = np.asmatrix(train_data[0])
        train_predictions = np.sign(average * np.transpose(train_data_matrix))
        train_error = calculate_error(train_predictions, train_data[1])

        test_data_matrix = np.asmatrix(test_data[0])
        test_predictions = np.sign(average * np.transpose(test_data_matrix))
        test_error = calculate_error(test_predictions, test_data[1])

        print(epoch, " Train error: ", train_error, " Test error: ", test_error)

    print("Weight vector: ", weight)
    print("Average: ", average)


if __name__ == '__main__':
    train_data = Read.read_data("bank-note/train.csv", 872)
    test_data = Read.read_data("bank-note/test.csv", 500)

    #if sys.argv[1] == "standard":
        #standard_perceptron()
    #elif sys.argv[1] == "votes":
        #voted_perceptron()
    #elif sys.argv[1] == "average":
    average_perceptron()
