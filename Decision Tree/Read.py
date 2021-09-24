"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
# List of columns as keys in car
key_list = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "label"]
attribute_val = {}
attribute_val["buying"] = ["vhigh", "high", "med", "low"]
attribute_val["maint"] = ["vhigh", "high", "med", "low"]
attribute_val["doors"] = ["2", "3", "4", "5more"]
attribute_val["persons"] = ["2", "4", "more"]
attribute_val["lug_boot"] = ["small", "med", "big"]
attribute_val["safety"] = ["low", "med", "high"]
attribute_val["label"] = ["unacc", "acc", "good", "vgood"]

# Q2 data
# key_list = ["O", "T", "H", "W", "Play?"]
# attribute_val = {}
# attribute_val["O"] = ["S", "O", "R"]
# attribute_val["T"] = ["H", "M", "C"]
# attribute_val["H"] = ["H", "N", "L"]
# attribute_val["W"] = ["S", "W"]
# attribute_val["Play?"] = ["n", "p"]

# initialize data
data = []


def read_data(path):
    # Add values to the data dictionary
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            row = {}
            for key in key_list:
                row[key] = None
            for i in range(len(key_list)):
                row[key_list[i]] = terms[i]
            data.append(row)

    return data