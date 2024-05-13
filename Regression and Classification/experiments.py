import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from id3 import build_tree, split_data, predict_answer

#tested parametres: max_depth; data_test_size, data_train_size

def calculate_accuracy(tree, test_data_m, label):
    correct_preditct = 0
    wrong_preditct = 0
    for set in test_data_m:
        result = predict_answer(tree, set)
        if result == set[label]:
            correct_preditct += 1
        else:
            wrong_preditct += 1
    accuracy = correct_preditct / (correct_preditct + wrong_preditct)
    return accuracy



def test_max_depth(data, attributes, data_splits_index_len, iterations, max_depth):
	target = "irradiat"

	y_values = []
	x_values = np.arange(0, max_depth, 1)
	plot_names = []
	for ds in range(len(data_splits_index_len)):
		data_split_index = data_splits_index_len[ds][0]
		data_max_len = data_splits_index_len[ds][1]
		data_train, data_test = split_data(data, data_split_index, data_max_len)
		plot_names.append(f"train data len: {len(data_train)}; test data len: {len(data_test)}")
		y_values_set = []
		for depth in range(0, max_depth):
			data_train, data_test = split_data(data, data_split_index, data_max_len)
			accuracy_total = 0
			for i in range(iterations):
				data_train, _ = split_data(data, data_split_index, data_max_len)
				tree = build_tree(data_train, attributes, target, depth)
				_, data_test = split_data(data, data_split_index, data_max_len)
				test_data_dict = []
				for d in data_test:
					test_data_dict.append(dict(zip(attributes,d)))
					
				accuracy = calculate_accuracy(tree, test_data_dict, target)
				accuracy_total += accuracy
			
			y_values_set.append(accuracy_total / iterations)
		y_values.append(y_values_set)


	plt.figure(figsize=(18, 12))
	plt.xlabel("Max depth")
	plt.ylabel("Accuracy")
	plt.xticks(x_values)
	print(plot_names)

	for i in range(len(y_values)):
		plt.plot(x_values, y_values[i], linewidth=3.5)

	plt.title(f"ID3 algorithm accuracy test for max_depth (training data length={len(data_train)}; test data length={len(data_test)}; iterations={iterations})", fontsize=16)
	plt.legend(plot_names, loc ="lower right")
	plt.show()


if __name__ == "__main__":
	plt.style.use('dark_background')
	matplotlib.use('tkagg')
	with open('breast-cancer.data', newline='') as file:
		data = [[]]
		for line in file:
			line = line.strip("\r\n")
			data.append(line.split(','))

	data.pop(0)
	attributes = ["Class","age","menopause","tumor-size","inv-nodes","node-caps","deg-malig","breast","breast-quad","irradiat"]
	# data.remove(attributes)
	

	test_max_depth(data, attributes, [(225, 283), (150, 200), (100, 125)], 20, 10)
