import math
import random
import numpy as np
from numpy.random import rand, randint

# factory_demand_units = {
#   	20: (1, 1),
#   	10: (-0.5, 1),
#   	5: (-1, -0.5),
# 	10: (1, -1)
# }


def calculate_manhatan_distance(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


def calculate_transportation_cost(factory_coords):
    total_cost = 0
    # for number, coords in factory_demand_units.items():
    #     print(number, coords, len(factory_demand_units))
    #     total_cost += number * (1 - math.e ** (-calculate_manhatan_distance(coords, factory_coords)))

    total_cost += 20 * (1 - math.e ** (-calculate_manhatan_distance((1, 1), factory_coords)))
    total_cost += 10 * (1 - math.e ** (-calculate_manhatan_distance((-0.5, 1), factory_coords)))
    total_cost += 5 * (1 - math.e ** (-calculate_manhatan_distance((-1, -0.5), factory_coords)))
    total_cost += 10 * (1 - math.e ** (-calculate_manhatan_distance((1, -1), factory_coords)))
    return total_cost


def roulette_selection(population):
	population_cost = []
	for unit in population:
		population_cost.append(calculate_transportation_cost(unit))
		
	total_cost = sum(population_cost)

	chromosome_probabilities = []

	probabilities = []
	for i in range(len(population)):
		probabilities.append(population_cost[i] / total_cost)
		
	probability_offset = 0
	for i in range(len(population)):
		probability = probability_offset + (population_cost[i] / total_cost)
		chromosome_probabilities.append(probability) 
		probability_offset += probability

	selected_indexes = []
	random_float = random.uniform(0, 1)
	for i in range(len(population)):
		if probabilities[i] > random_float:
			break; 
		selected_indexes.append(population[i])
	return selected_indexes

def roulette_selection2(population):
	population_cost = []
	for unit in population:
		population_cost.append(1 / calculate_transportation_cost(unit)) # 1 / cost   because goal is to minimize
	total_cost = sum(population_cost)
	probabilities = []
	for i in range(len(population)):
		probabilities.append(population_cost[i] / total_cost)
	return [population[np.random.choice(len(population), p=probabilities)] for _ in range(len(population))]


def one_point_crossover(parent1, parent2):
	child1, child2 = parent1, parent2
	child1 = (parent1[0], parent2[1])
	child2 = (parent2[0], parent1[1])
	return child1, child2


def gaussian_mutation(unit, mutation_rate):
	return (unit[0] + random.uniform(-1, 1) * mutation_rate, unit[1] + random.uniform(-1, 1) * mutation_rate)



def genetic_algorithm(cost_function, coords_range, iterations, population_size, mutation_rate):
	population = [(random.uniform(coords_range[0], coords_range[1]), random.uniform(coords_range[0], coords_range[1])) for _ in range(population_size)]
	best, best_score = (0, 0), cost_function(population[0]) # keep track of best solution

	for iteration in range(iterations):
		scores = [cost_function(item) for item in population]

		for i in range(population_size):
			if scores[i] < best_score:
				best, best_score = population[i], scores[i]
				print(f"Iteration: {iteration}   with new best score: {scores[i]}   with coords: {population[i]}")

		selected = roulette_selection2(population)
		children = []
		for i in range(0, population_size, 2):
			if (i+1 >= population_size):
				parent1, parent2 = selected[i], selected[0]
			else:
				parent1, parent2 = selected[i], selected[i+1]

			for child in one_point_crossover(parent1, parent2):
				child = gaussian_mutation(child, mutation_rate)
				children.append(child)
		population = children

	return best, best_score
 


if __name__ == "__main__":
	iterations = 500
	coords_range = [-1,1]
	pop_size = 500
	mutation_rate = 0.25

	best, best_score = genetic_algorithm(calculate_transportation_cost, coords_range, iterations, pop_size, mutation_rate)
	print(f"Best score is: {best_score}  with coordinates: {best}")

	print(calculate_transportation_cost((1,1)))
