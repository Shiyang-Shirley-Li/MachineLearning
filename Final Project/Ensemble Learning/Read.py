import statistics
import numpy as np

data_attributes = [
    ["numeric", "less", "bigger"],
    ["workclass", "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay",
     "Never-worked"],
    ["numeric", "less", "bigger"],
    ["education", "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th",
     "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"],
    ["numeric", "less", "bigger"],
    ["marital-status", "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent",
     "Married-AF-spouse"],
    ["occupation", "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty",
     "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
     "Protective-serv", "Armed-Forces"],
    ["relationship", "Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"],
    ["race", "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"],
    ["sex", "Female", "Male"],
    ["numeric", "less", "bigger"],
    ["numeric", "less", "bigger"],
    ["numeric", "less", "bigger"],
    ["native-country", "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)",
     "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica",
     "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti",
     "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago",
     "Peru", "Hong", "Holand-Netherlands"]
]

labels = [-1, 1]


def read_data(path, deal_with_missing, train):
    s = []
    with open(fp, 'r') as f:
        num_columns = 0
        for line in f:
            terms = line.strip().split(',')
            num_columns = len(terms)

        s = [[] for _ in range(num_columns)]

        for line in f:
            terms = line.strip().split(',')
            for i in range(num_columns):
                s[i].append(terms[i])

    attributes = data_attributes
    temp = change_numeric_to_binary(s, attributes)
    if deal_with_missing:
        s = change_missing_to_majority(temp, attributes, train) #?????
    return s


def change_numeric_to_binary(s, attributes):
    for i in range(len(attributes)):
        if attributes[i][0] == "numeric":
            s_i_ints = list(map(int, s[i]))
            median = statistics.median(s_i_ints)
            
            attributes[i][0] = str(median)

            for j in range(len(s[i])):
                if int(s[i][j]) > int(attributes[i][0]):
                    s[i][j] = "bigger"
                else:
                    s[i][j] = "less"

        #elif _is_numeric_attribute(attributes[i]):#?????
            #s[i] = _update_numeric_attributes(s[i], attributes[i])
    return s


# def _is_numeric_attribute(attribute):
#     """Check if a given attribute in the bank list is numeric."""
#     try:
#         int(attribute[0])
#         return True
#     except ValueError:
#         return False


def change_missing_to_majority(s, attributes, train):
    majority = []
    for i in range(len(attributes)):
        if train:
            majority.append("")
            if "?" in attributes[i]:
                majority_attribute = majority_attribute_value(s[i], attributes[i])
                majority[i] = majority_attribute

                for j in range(len(s[i])):
                    if s[i][j] == "?":
                        s[i][j] = majority_attribute

        elif "?" in attributes[i]:
            for j in range(len(s[i])):
                if s[i][j] == "?":
                    s[i][j] = majority[i]
    return s


def majority_attribute_value(subset, attribute):
    count = [0 for _ in range(len(attribute))]

    for value in subset:
        for i in range(len(attribute)):
            if value == attribute[i] and attribute[i] != "?":
                count[i] += 1
                break

    index = count.index(max(count))
    return attribute[index]

