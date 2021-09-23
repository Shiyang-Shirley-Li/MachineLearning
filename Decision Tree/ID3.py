"""
@author: Shirley (Shiyang) Li

ID3 algorithm by using information gain, majority error, and gini index
"""

import Read
import math

# Variables
train_data = Read.read_data("Test/train.csv")
#max_depth = input("Enter your maximum tree depth: ")


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
def ID3(s, attributes, label, level, parent):
    # if all examples have the same label, return a leaf node with the label

    # if attributes empty or reach the maximum tree depth,
    # return a leaf node with the most common label
    if len(attributes) == 0 or level == max_depth:
        node = Node(s, parent, True)
        node.set_label(most_common_label)
        return node

    else:
        # Create a root node for the tree
        node = Node(s, parent, False)
        #best_attribute = get_best_attribute()
        #node.set_attribute(best_attribute)

        #for value in node.attribute:



if __name__ == '__main__':
    print(gini_index_gain(train_data, "T"))







