import random as rand

# each item : (wight,value)
ITEMS = [
	(5, 10), 
	(4, 40), 
	(6, 30), 
	(3, 5),
	(2, 60), 
	(1, 20),
	(8, 80),
 	(7, 55),
	(9, 65), 
	(6, 85), 
	(7, 25), 
	(10, 50),
	(12, 10), 
	(4, 75), 
	(10, 100), 
	(8, 95),
	(3, 30), 
	(5, 65), 
	(7, 40), 
	(9, 55)
]

POP_SIZE = 100
GENOME_SIZE = 20
CAPACITY = 50
MUTATION_RATE = 0.05
MAXIMUM_GENERATIONS = 50000

def init_population(pop_size, genome_size):
	population = []
	for _ in range(pop_size):
		individual = []
		for _ in range(genome_size):
			gene = rand.choice([0, 1])
			individual.append(gene)
		population.append(individual)
	return population

def fitness_calc(individual):
	total_weight = sum(individual[i] * ITEMS[i][0] for i in range(len(individual)))
	total_value = sum(individual[i] * ITEMS[i][1] for i in range(len(individual)))
	if total_weight > CAPACITY:
		return 0  
	return total_value

def selection(population, fitnesses):
	tournament = rand.sample(range(len(population)), k=3)
	tournament_fitness = [fitnesses[i] for i in tournament]
	winner_index = tournament[tournament_fitness.index(max(tournament_fitness))]
	return population[winner_index]

def mutate(individual):
	return [(gene if rand.random() > MUTATION_RATE else 1 - gene) for gene in individual]

def crossover(parent1, parent2):
	xo_point = rand.randint(1, len(parent1) - 1)
	offspring1 = parent1[:xo_point] + parent2[xo_point:]
	offspring2 = parent2[:xo_point] + parent1[xo_point:]
	return [offspring1, offspring2]

def main():
	population = init_population(POP_SIZE, GENOME_SIZE)
	generation_index = 0
	overall_best_individual = None
	overall_best_fitness = 0
	overall_best_weight = 0
	overal_best_generation = 0
	
	while generation_index <= MAXIMUM_GENERATIONS:
		population_fitness = [fitness_calc(individual) for individual in population]
		
		best_fitness = max(population_fitness)
		best_individual = population[population_fitness.index(best_fitness)]
		best_weight = sum(best_individual[i] * ITEMS[i][0] for i in range(GENOME_SIZE))
		
		print(f"Generation {generation_index}: Best fitness = {best_fitness}, Solution = {best_individual}")
		
		if best_fitness > 0 and best_weight <= CAPACITY:
			if (best_fitness > overall_best_fitness):
				overall_best_individual = best_individual
				overall_best_fitness = best_fitness
				overall_best_weight = best_weight
				overal_best_generation = generation_index
				print("New best found:", overall_best_individual)
				print("Total value:", overall_best_fitness)
				print("Total weight:", overall_best_weight)
			

		nextgen_population = []
		for _ in range(int(POP_SIZE / 2)):
			parent1 = selection(population, population_fitness)
			parent2 = selection(population, population_fitness)
			offspring1, offspring2 = crossover(parent1, parent2)
			nextgen_population += [mutate(offspring1), mutate(offspring2)]
		
		population = nextgen_population
		generation_index += 1

	print("-"*20)
	print("Overall best solution:", overall_best_individual)
	print("Found in generation", overal_best_generation)
	print("Total value:", overall_best_fitness)
	print("Total weight:", overall_best_weight)

if __name__ == "__main__":
	main()