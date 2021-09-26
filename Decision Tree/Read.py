"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
import statistics

#List of columns as keys in car
key_list = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "label"]
attribute_val = {}
attribute_val["buying"] = ["vhigh", "high", "med", "low"]
attribute_val["maint"] = ["vhigh", "high", "med", "low"]
attribute_val["doors"] = ["2", "3", "4", "5more"]
attribute_val["persons"] = ["2", "4", "more"]
attribute_val["lug_boot"] = ["small", "med", "big"]
attribute_val["safety"] = ["low", "med", "high"]
attribute_val["label"] = ["unacc", "acc", "good", "vgood"]

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

# Q2 data for test
# key_list = ["O", "T", "H", "W", "Play?"]
# attribute_val = {}
# attribute_val["O"] = ["S", "O", "R"]
# attribute_val["T"] = ["H", "M", "C"]
# attribute_val["H"] = ["H", "N", "L"]
# attribute_val["W"] = ["S", "W"]
# attribute_val["Play?"] = ["n", "p"]

def read_data(path, data_type):
    # initialize data
    data = []
    # Add values to the data dictionary
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            row = {}
            if data_type == "car":
                for key in key_list:
                    row[key] = None
                for i in range(len(key_list)):
                    row[key_list[i]] = terms[i]
                data.append(row)
            elif data_type == "bank":
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


# attribute value missing
def unknown_to_majority(d, attributes, train_majority):
    for i in range(len(d)):  # each row
        for j in range(len(attributes)):  # each column
            if d[i][(list(d[i].keys())[j])] == "unknown":
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


