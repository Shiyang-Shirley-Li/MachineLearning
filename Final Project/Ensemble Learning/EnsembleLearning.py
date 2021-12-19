import math
import ID3

T = 500
train_data = ID3.train_data
test_data = ID3.test_data
m = len(train_data)
predictions = [[]]
weights = [[]]
votes = []
for j in range(len(train_data)):
    weights[0].append(1/m)
trees = []#store each tree stump
total_attributes = ID3.total_attributes
train_tree = ID3.train(train_data)


def dt_predict_result(s, tree):
    dt_predict = []
    true_val = []
    for i in range(len(s)):
        row_attributes = []
        for key in total_attributes:
            row_attributes.append(s[i][key])
        dt_predict.append(ID3.predict_result(row_attributes, tree.root)[0])
        true_val.append(row_attributes[-1])
    return dt_predict, true_val


def convert_to_num(s):
    y = []
    for val in s:
        if val == "no":
            y.append(-1)
        else:
            y.append(1)
    return y


def ada_boost():
    train_tree_true = dt_predict_result(train_data, train_tree)[1]
    y_train = convert_to_num(train_tree_true)
    test_tree_true = dt_predict_result(test_data, train_tree)[1]
    y_test = convert_to_num(test_tree_true)

    # Print ada train and test error
    ada_train_err = ""
    ada_test_err = ""
    for t in range(T):
        ada_train_result = ada_boost_train(y_train, t)


def ada_boost_train(y, t):
    tree = ID3.train(train_data, weights[t]) #how to relate to t????????????? weights???
    trees.append(tree)

    predictions[t] = convert_to_num(dt_predict_result(train_data, tree)[0])
    error = compute_error(y, t)
    votes.append(compute_vote(error))
    weights[t+1].append(compute_weights(y, t+1)) #???????????

    final_hyp = compute_final_hyp(predictions)

    return final_hyp


def compute_error(y, t):
    sum = 0
    for i in range(len(y)):
        sum += weights[t][i] * y[i] * predictions[t][i]
    return 1 / 2 - 1 / 2 * sum


def compute_vote(error):
    return 1/2 * math.log((1-error)/error)


def compute_weights(y, t):
    error = compute_error(y, t-1)
    vote = compute_vote(error)
    z = 0
    for k in range(len(y)):
        z += weights[t-1][k]

    weight = []
    for i in range(len(y)):
        weight.append(weights[t-1][i] * math.exp(-vote * y[i] * predictions[t-1][i])/z)

    return weight


def compute_final_hyp(_predictions):
    temp = [[]]
    for i in range(len(votes)):
        temp_arr = []
        for k in range(len(votes[0])):
            temp_arr = votes[i][k] * _predictions[i][k]
        temp.append(temp_arr)


if __name__ == '__main__':
    ada_boost()