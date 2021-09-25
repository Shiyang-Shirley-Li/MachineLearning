"""
@author: Shirley (Shiyang) Li

ID3 algorithm by using information gain, majority error, and gini index
"""

import Read
import math

# Variables
train_data = Read.read_data("car/train.csv")
test_data = Read.read_data("car/test.csv")
max_depth = int(input("Enter your maximum tree depth: "))
total_attributes = Read.key_list[0:len(Read.key_list)]
total_label_num = len(train_data)
attribute_val_dict = Read.attribute_val

# Information Gain

# Calculate entropy

# the total entropy of set s
def current_entropy(s):
    total_label_num = len(s)
    label_name = []
    for i in range(total_label_num):
        label_name.append(s[i][(list(s[i].keys())[-1])])
    labels = set(label_name)
    labels_num = {}
    for key in labels:
        labels_num[key] = 0

    for i in range(total_label_num):
        labels_num[s[i][(list(s[i].keys())[-1])]] += 1

    total_entropy = 0
    for key in labels:
        fraction = labels_num[key]/total_label_num
        total_entropy-= fraction * math.log(fraction, 2)
    return total_entropy


# the entropy of an attribute in set s
def expected_entropy(s, attribute):
    num = len(s)
    examples = set()
    for i in range(num):
        examples.add(s[i].get(attribute))

    examples_num = {}
    for key in examples:
        examples_num[key] = 0

    for i in range(num):
        examples_num[s[i].get(attribute)] += 1

    exp_entropy = 0
    for key in examples:
        subset = []
        for i in range(num):
            if s[i].get(attribute) == key:
                subset.append(s[i])
        exp_entropy += examples_num[key]/num * current_entropy(subset)

    return exp_entropy


# the information gain of an attribute
def info_gain(s, attribute):
    return current_entropy(s) - expected_entropy(s, attribute)


# Majority Error = 1 - num of majority label/total num of label
def current_majority_error(s):
    return 1 - most_common_label(s)[1]

# the majority error of an attribute in set s
def expected_majority_error(s, attribute):
    num = len(s)
    examples = set()
    for i in range(num):
        examples.add(s[i].get(attribute))

    examples_num = {}
    for key in examples:
        examples_num[key] = 0

    for i in range(num):
        examples_num[s[i].get(attribute)] += 1

    majority_error = 0
    for key in examples:
        subset = []
        for i in range(num):
            if s[i].get(attribute) == key:
                subset.append(s[i])
        majority_error += examples_num[key] / num * current_majority_error(subset)

    return majority_error


# the gain of an attribute by using ME
def majority_error_gain(s, attribute):
    return current_majority_error(s) - expected_majority_error(s, attribute)


# Gini Index
def current_gini_index(s):
    total_label_num = len(s)
    label_name = []
    for i in range(total_label_num):
        label_name.append(s[i][(list(s[i].keys())[-1])])
    labels = set(label_name)
    labels_num = {}
    for key in labels:
        labels_num[key] = 0

    for i in range(total_label_num):
        labels_num[s[i][(list(s[i].keys())[-1])]] += 1

    square_value = 0
    for key in labels:
        fraction = labels_num[key] / total_label_num
        square_value += pow(fraction, 2)
    return 1 - square_value


# the entropy of an attribute in set s
def expected_gini_index(s, attribute):
    num = len(s)
    examples = set()
    for i in range(num):
        examples.add(s[i].get(attribute))

    examples_num = {}
    for key in examples:
        examples_num[key] = 0

    for i in range(num):
        examples_num[s[i].get(attribute)] += 1

    exp_gini_index = 0
    for key in examples:
        subset = []
        for i in range(num):
            if s[i].get(attribute) == key:
                subset.append(s[i])
        exp_gini_index += examples_num[key]/num * current_gini_index(subset)

    return exp_gini_index


# the information gain of an attribute
def gini_index_gain(s, attribute):
    return current_gini_index(s) - expected_gini_index(s, attribute)



# return a tuple of most common label and its percentage of a set s
def most_common_label(s):
    total_label_num = len(s)
    label_name = []
    for i in range(total_label_num):
        label_name.append(s[i][(list(s[i].keys())[-1])])
    labels = set(label_name)
    labels_num = {}
    for key in labels:
        labels_num[key] = 0

    for i in range(total_label_num):
        labels_num[s[i][(list(s[i].keys())[-1])]] += 1

    largest_frac = 0
    most_common = None
    for key in labels:
        fraction = labels_num[key] / total_label_num
        if fraction > largest_frac:
            most_common = key
            largest_frac = fraction
    return (most_common, largest_frac)


total_most_common_label = most_common_label(train_data) #??????


# Return a dictionary having attribute as its key and the value of attribute
# as value.
# def attribute_value_dictionary(s, attributes):
#     attribute_val = {}
#     total_label_num = len(s)
#     for j in range(len(attributes)):
#         key = attributes[j]
#         attribute_val[key] = set()
#         for i in range(total_label_num):
#             attribute_val[key].add(s[i][(list(s[i].keys())[j])])
#     return attribute_val
#
#
# attribute_val_dict = attribute_value_dictionary(train_data, total_attributes[0:len(total_attributes)-1])



# Data Structures
class Node:
    # Contains an attribute, different branches, subset, parent, label (if it is a
    # leaf node)
    def __init__(self, subset, parent, is_leaf):
        self.attribute = None
        self.branches = {}
        self.subset = subset
        self.parent = parent
        self.label = None
        self.is_leaf = is_leaf

    def set_attribute(self, attribute):
        self.attribute = attribute

    # each branch has its own value and node
    def add_branch(self, value, node):
        self.branches[value] = node

    # if it is a leaf node, set a label for it
    def set_label(self, label):
        self.label = label

class Tree:
    def __init__(self):
        self.max_depth = max_depth
        self.root = None

    def set_root(self, node):
        self.root = node


# ID3 Algorithm
def ID3(s, attributes, level, parent):
    # if all examples have the same label, return a leaf node with the label
    total_label_num = len(s)
    label_name = []
    for i in range(total_label_num):
        label_name.append(s[i][(list(s[i].keys())[-1])])
    labels = set(label_name)
    if len(labels) == 1:
        node = Node(s, parent, True)
        node.set_label(list(labels)[0])
        return node

    # if attributes empty or reach the maximum tree depth,
    # return a leaf node with the most common label
    if len(attributes) == 0 or level == max_depth:
        node = Node(s, parent, True)
        node.set_label(most_common_label(s))#??????
        return node

    else:
        # Create a root node for the subtree
        node = Node(s, parent, False)
        best_attribute = get_best_attribute(s, attributes)
        node.set_attribute(best_attribute)

        for value in attribute_val_dict[node.attribute]:
            subset_v = get_s_v(node, node.attribute, value)

            if len(subset_v) == 0:
                label = most_common_label(s)
                child_node = Node({}, node, True)
                child_node.set_label(label)
                node.add_branch(value, child_node)
            else:
                attr = attributes.copy() #remain original attributes
                attr.remove(node.attribute)
                child_node = ID3(subset_v, attr, level + 1, node)
                node.add_branch(value, child_node)
        return node


# Return the best attribute that best splits s by using purity
def get_best_attribute(s, attributes, purity_type="entropy"):
    gains = []
    for attribute in attributes:
        if purity_type == "entropy":
            gains.append(info_gain(s, attribute))
        elif purity_type == "ME":
            gains.append(majority_error_gain(s, attribute))
        elif purity_type == "GI":
            gains.append(gini_index_gain(s, attribute))
    max_index = gains.index(max(gains))
    return attributes[max_index]


# Return the subset for an attribute value
def get_s_v(node, attribute, value):
    attr_index = total_attributes.index(attribute)
    subset_v = []
    subset_indices = []
    for i in range(len(node.subset)):
        val = node.subset[i][(list(node.subset[i].keys())[attr_index])]
        if node.subset[i][(list(node.subset[i].keys())[attr_index])] == value:

            #row[value] = node.subset[i][(list(node.subset[i].keys())[-1])]
            row = {}
            for key in total_attributes:
                row[key] = None
            for j in range(len(total_attributes)):
                row[total_attributes[j]] = node.subset[i][(list(node.subset[i].keys())[j])]
            subset_v.append(row)
            subset_indices.append(i)
    return subset_v


def train(s):
    train_tree = Tree()
    train_tree.set_root(ID3(train_data, total_attributes[0:len(total_attributes)-1], 1, None))
    return train_tree


# Prediction error for 2a
def average_prediction_error(s, root_node):
    wrong_count = 0
    for i in range(len(s)):
        row_attributes = []
        for key in total_attributes:
            row_attributes.append(s[i][key])
        if row_attributes[-1] != predict_result(row_attributes, root_node):
            wrong_count += 1

    return wrong_count/len(s)


def predict_result(attributes, node):
    if not node.is_leaf:
        attr_index = total_attributes.index(node.attribute)
        child = node.branches[attributes[attr_index]]
        return predict_result(attributes, child)
    else:
        return node.label


if __name__ == '__main__':
    tree = train(train_data)
    err = average_prediction_error(train_data, tree.root)
    err_test = average_prediction_error(test_data, tree.root)
    print(err)
    print(err_test)
    i = 0

# purity type, max tree depth, data





