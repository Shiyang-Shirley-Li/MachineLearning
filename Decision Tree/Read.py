"""
@author: Shirley (Shiyang) Li

Read data from a csv file path as a dictionary
"""
# List of columns as keys in car
# key_list = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "label"]

key_list = ["O", "T", "H", "W", "Play?"]

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