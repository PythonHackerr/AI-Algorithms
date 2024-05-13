import math
import random


def build_tree(data, params, target_label, max_depth=10, curr_depth=0):
    data = data.copy()
    vals = [set[params.index(target_label)] for set in data]
    default = get_most_frequent_value(data, params, target_label)

    if not data or (len(params) - 1) <= 0:
        return default

    if vals.count(vals[0]) == len(vals) or max_depth <= curr_depth:
        return vals[0]
    else:
        best_param = best_parametr(data, params, target_label)
        tree = {best_param: {}}

        for value in generate_values(data, params, best_param):
            examples = generate_examples(data, params, best_param, value)
            newAttr = params[:]
            newAttr.remove(best_param)
            tree[best_param][value] = build_tree(examples, newAttr, target_label, max_depth, curr_depth + 1)
    
    return tree


def get_entropy(params, data, target_label):
    frequency = {}
    entropy = 0.0
    i = 0
    for label in params:
        if (target_label == label):
            break
        ++i
    for set in data:
        if (set[i] in frequency):
            frequency[set[i]] += 1.0
        else:
            frequency[set[i]]  = 1.0

    for freq in frequency.values():
        entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return entropy


def get_info_gain(params, data, attr, target_label):
    frequency = {}
    entropy = 0.0

    for set in data:
        if (set[params.index(attr)] in frequency):
            frequency[set[params.index(attr)]] += 1.0
        else:
            frequency[set[params.index(attr)]] = 1.0

    for val in frequency.keys():
        val_prob = frequency[val] / sum(frequency.values())
        data_subset = [set for set in data if set[params.index(attr)] == val]
        entropy += val_prob * get_entropy(params, data_subset, target_label)

    return (get_entropy(params, data, target_label) - entropy)


def get_most_frequent_value(data, params, target_label):
    frequency = {}
    for set in data:
        if (set[params.index(target_label)] in frequency):
            frequency[set[params.index(target_label)]] += 1 
        else:
            frequency[set[params.index(target_label)]] = 1
    max_frequency = 0
    most_frequent = ""
    for key in frequency.keys():
        if frequency[key] > max_frequency:
            max_frequency = frequency[key]
            most_frequent = key
    return most_frequent


def best_parametr(data, params, target_label):
    best = params[0]
    maxGain = 0;
    for attr in params:
        newGain = get_info_gain(params, data, attr, target_label) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best


def generate_values(data, params, attr):
    index = params.index(attr)
    values = []
    for set in data:
        if set[index] not in values:
            values.append(set[index])
    return values


def generate_examples(data, params, best, val):
    examples = [[]]
    index = params.index(best)
    for set in data:
        if (set[index] == val):
            new_set = []
            for i in range(0,len(set)):
                if(i != index):
                    new_set.append(set[i])
            examples.append(new_set)
    examples.remove([])
    return examples
    

def predict_answer(tree, test_set):
    if not isinstance(tree, dict): # check if leaf node
        return tree
    else:
        root_node = next(iter(tree))
        feature_value = test_set[root_node]
        if feature_value in tree[root_node]: # check if feature is in current node
            return predict_answer(tree[root_node][feature_value], test_set)
        else:
            return None


def split_data(data, data_split_index, data_max_len = 9999999):
    temp_data = data.copy()
    random.shuffle(temp_data)
    first_part = temp_data[:data_split_index]
    second_part = temp_data[data_split_index:data_max_len]
    return first_part, second_part



if __name__ == '__main__':
    with open('breast-cancer.data', newline='') as file:
        data = [[]]
        for line in file:
            line = line.strip("\r\n")
            data.append(line.split(','))
    data.pop(0)
    attributes = ["Class","age","menopause","tumor-size","inv-nodes","node-caps","deg-malig","breast","breast-quad","irradiat"]#data[0]
    target_label = "irradiat"

    data_train, data_test = split_data(data, 200)

    tree = build_tree(data_train, attributes, target_label)

    test={'Class':'no-recurrence-events','age':'70-79','menopause':'ge40','tumor-size':'30-34',
    "inv-nodes":"0-2", 'node-caps':'no','deg-malig':'1','breast':'right','breast-quad':'right_up'}
    answer = predict_answer(tree, test)
    print(f"Answer is: {answer}")