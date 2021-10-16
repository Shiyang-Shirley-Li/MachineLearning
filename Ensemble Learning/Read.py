"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
import statistics

#List of columns as keys in bank
key_list_bank = ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day",
                 "month", "duration", "campaign", "pdays", "previous", "poutcome", "label"]
attribute_val_bank = {}
attribute_val_bank["age"] = ["numeric", "less", "bigger"]
attribute_val_bank["job"] = ["nn", "admin.", "unknown", "unemployed", "management", "housemaid", "entrepreneur", "student",
                                       "blue-collar", "self-employed", "retired", "technician", "services"]
attribute_val_bank["marital"] = ["nn", "married", "divorced", "single"]
attribute_val_bank["education"] = ["nn", "unknown", "secondary", "primary", "tertiary"]
attribute_val_bank["default"] = ["nn", "yes", "no"]
attribute_val_bank["balance"] = ["numeric", "less", "bigger"]
attribute_val_bank["housing"] = ["nn", "yes", "no"]
attribute_val_bank["loan"] = ["nn", "yes", "no"]
attribute_val_bank["contact"] = ["nn", "unknown", "telephone", "cellular"]
attribute_val_bank["day"] = ["numeric", "less", "bigger"]
attribute_val_bank["month"] = ["nn", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
attribute_val_bank["duration"] = ["numeric", "less", "bigger"]
attribute_val_bank["campaign"] = ["numeric", "less", "bigger"]
attribute_val_bank["pdays"] = ["numeric", "less", "bigger"]
attribute_val_bank["previous"] = ["numeric", "less", "bigger"]
attribute_val_bank["poutcome"] = ["nn", "unknown", "other", "failure", "success"]
attribute_val_bank["label"] = ["nn", "yes", "no"]

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


