import numpy as np
import matplotlib.pyplot as plt
from genetic_algorithm import genetic_algorithm, calculate_transportation_cost


def mutation_rate_experiment(mutation_rate_values):
	iterations = 100
	population_size = 10

	results = []
	for mutation_rate in mutation_rate_values:
		best, best_score = genetic_algorithm(calculate_transportation_cost, coords_range, iterations, population_size, mutation_rate)
		results.append(best_score)

	data = dict(zip(results, mutation_rate_values))

	scores = list(data.keys())
	mutation_rates = list(data.values())
	
	fig = plt.figure(figsize = (20, 10))
	
	# creating the bar plot
	plt.bar(mutation_rates, scores, color ='maroon',
			width = 0.0015)
	
	plt.xlabel("mutation rates")
	plt.ylabel("scores")
	plt.title(f"mutation rate experiment for population_size: {population_size}; iterations: {iterations}")
	plt.show()



def population_size_experiment(population_size_values):
	iterations = 25
	mutation_rate = 0.25

	results = []
	for population_size in population_size_values:
		best, best_score = genetic_algorithm(calculate_transportation_cost, coords_range, iterations, population_size, mutation_rate)
		results.append(best_score)

	data = dict(zip(results, population_size_values))

	scores = list(data.keys())
	population_sizes = list(data.values())
	
	fig = plt.figure(figsize = (20, 10))
	
	# creating the bar plot
	plt.bar(population_sizes, scores, color ='green',
			width = 0.4)
	
	plt.xlabel("population_sizes")
	plt.ylabel("scores")
	plt.title(f"population size experiment for mutation_rate: {mutation_rate}; iterations: {iterations}")
	plt.show()



def iterations_experiment(iterations_values):
	population_size = 50
	mutation_rate = 0.25

	results = []
	for iterations in iterations_values:
		best, best_score = genetic_algorithm(calculate_transportation_cost, coords_range, iterations, population_size, mutation_rate)
		results.append(best_score)

	data = dict(zip(results, iterations_values))

	scores = list(data.keys())
	iterations = list(data.values())
	
	fig = plt.figure(figsize = (20, 10))
	
	# creating the bar plot
	plt.bar(iterations, scores, color ='blue',
			width = 0.4)
	
	plt.xlabel("iterations")
	plt.ylabel("scores")
	plt.title(f"iterations experiment for mutation_rate: {mutation_rate}; population_size: {population_size}")
	plt.show()



if __name__ == "__main__":
	plt.style.use('dark_background')

	coords_range = [-1,1]

	# mutation_rate_values = np.arange(0.001, 1, 0.0025)
	# mutation_rate_experiment(mutation_rate_values)

	# population_size_values = np.arange(1, 100, 1)
	# population_size_experiment(population_size_values)

	iterations_values = np.arange(1, 200, 1)
	iterations_experiment(iterations_values)