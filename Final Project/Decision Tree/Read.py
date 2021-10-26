"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
import statistics

#List of columns as keys in bank
key_list_bank = ["age","workclass","fnlwgt","education","education.num","marital.status","occupation","relationship",
                 "race","sex","capital.gain","capital.loss","hours.per.week","native.country","income>50K"]
attribute_val_bank = {}
attribute_val_bank["age"] = ["numeric", "less", "bigger"]
attribute_val_bank["workclass"] = ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov",
                                   "State-gov", "Without-pay", "Never-worked"]
attribute_val_bank["fnlwgt"] = ["numeric", "less", "bigger"]
attribute_val_bank["education"] = ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc",
                                   "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"]
attribute_val_bank["education.num"] = ["numeric", "less", "bigger"]
attribute_val_bank["marital.status"] = ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed",
                                        "Married-spouse-absent", "Married-AF-spouse"]
attribute_val_bank["occupation"] = ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty",
                                    "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving",
                                    "Priv-house-serv", "Protective-serv", "Armed-Forces"]
attribute_val_bank["relationship"] = ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"]
attribute_val_bank["race"] = ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"]
attribute_val_bank["sex"] = ["Female", "Male"]
attribute_val_bank["capital.gain"] = ["numeric", "less", "bigger"]
attribute_val_bank["capital.loss"] = ["numeric", "less", "bigger"]
attribute_val_bank["hours.per.week"] = ["numeric", "less", "bigger"]
attribute_val_bank["native.country"] = ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany",
                                        "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China",
                                        "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica",
                                        "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
                                        "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala",
                                        "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago",
                                        "Peru", "Hong", "Holand-Netherlands"]
attribute_val_bank["income>50K"] = ["0", "1"]


def read_data(path):
    # initialize data
    data = []
    # Add values to the data dictionary
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            row = {}

            for key in key_list_bank:
                row[key] = None
            for i in range(len(key_list_bank)):
                row[key_list_bank[i]] = terms[i]
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


