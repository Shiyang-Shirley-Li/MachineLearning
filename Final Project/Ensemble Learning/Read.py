"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
import statistics


#List of columns as keys
key_list= ["age", "workclass", "fnlwgt", "education", "education.num", "marital.status", "occupation",
                 "relationship", "race", "sex", "capital.gain", "capital.loss", "hours.per.week", "native.country"]
attribute_val = {}
attribute_val["age"] = ["numeric", "less", "bigger"],
attribute_val["workclass"] = ["nn", "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov",
                                   "State-gov", "Without-pay", "Never-worked"],
attribute_val["fnlwgt"] = ["numeric", "less", "bigger"],
attribute_val["education"] = ["nn", "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm",
                                 "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate",
                                 "5th-6th", "Preschool"],
attribute_val["education.num"] = ["numeric", "less", "bigger"],
attribute_val["marital-status"] = ["nn", "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed",
                                        "Married-spouse-absent", "Married-AF-spouse"],
attribute_val["occupation"] = ["nn", "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial",
                                    "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
                                    "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv",
                                    "Armed-Forces"],
attribute_val["relationship"] = ["nn", "Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"],
attribute_val["race"] = ["nn", "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"],
attribute_val["sex"] = ["nn", "Female", "Male"],
attribute_val["capital.gain"] = ["numeric", "less", "bigger"],
attribute_val["capital.loss"] = ["numeric", "less", "bigger"],
attribute_val["hours.per.week"] = ["numeric", "less", "bigger"],
attribute_val["native-country"] = ["nn", "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", 
                                        "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", 
                                        "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", 
                                        "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", 
                                        "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", 
                                        "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"]
attribute_val["label"] = ["nn", "1", "0"]


def read_data(path, train = True):
    # initialize data
    data = []
    # Add values to the data dictionary
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            row = {}
            
            if train:
                for key in key_list:
                    row[key] = None
                for i in range(len(key_list)):
                    row[key_list[i]] = terms[i]
                data.append(row)
            else:
                for key in key_list[:len(key_list) - 1]:
                    row[key] = None
                for i in range(len(key_list)-1):
                    row[key_list[i]] = terms[i]
                data.append(row)
    return data


# Convert a numerical feature to a binary one for Q3
def change_numeric_to_binary(original_data, attributes):
    for i in range(len(attributes)):
        if list(attributes.values())[i][0] == "numeric":
            median = calculate_median(original_data, i)
            original_data = update_numeric_to_binary(original_data, i, median)
    return original_data


def calculate_median(d, i):
    all_values_i = []
    for j in range(len(d)):
        all_values_i.append(int(d[j][(list(d[j].keys())[i])]))
    median = statistics.median(all_values_i)
    return median


def update_numeric_to_binary(d, i, med):
    for j in range(len(d)):
        if int(d[j][(list(d[j].keys())[i])]) > med:
            d[j][(list(d[j].keys())[i])] = "bigger"
        else:
            d[j][(list(d[j].keys())[i])] = "less"
    return d


# attribute value missing
def unknown_to_majority(d, attributes, train_majority):
    for i in range(len(d)):  # each row
        for j in range(len(attributes)):  # each column
            if d[i][(list(d[i].keys())[j])] == "?":
                d[i][(list(d[i].keys())[j])] = train_majority[attributes[j]]
    return d


def get_majority_attribute_val(d, attributes):
    attribute_type_count = {}
    i = 0
    for attribute in list(attributes.keys()):
        attribute_type_count[attribute] = []
        for attribute_type in list(attributes.get(attribute)):
            attribute_type_count[attribute].append({attribute_type: 0})
        i+=1

    for j in range(len(d)): # each row
        for k in range(len(attributes)): # each column
            key = [d[j][(list(d[j].keys())[k])]][0]
            for l in range(len(attribute_type_count[(list(attributes.keys())[k])])): # length of attribute values
                if key == list(attribute_type_count[(list(attributes.keys())[k])][l].keys())[0]:
                    attribute_type_count[(list(attributes.keys())[k])][l][d[j][(list(d[j].keys())[k])]] += 1

    # attribute_majority = {}
    # for index in range(len(attributes)):
    #     max = 0
    #     for val_l in range(len(attribute_type_count[(list(attributes.keys())[index])])):  # length of attribute values
    #         if attribute_type_count[(list(attributes.keys())[k])][l][d[j][(list(d[j].keys())[index])]]
    #     attribute_majority[attributes[index]] =
    return attribute_type_count


