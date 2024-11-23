from  Population import Population
from animation import animate
# def main():
#     population_size = 50
#     population = Population(population_size)
#     while True:
#         population.check_population()
#         bestSolution, maxFit= population.evaluate( )
#         print("Best solution: ", maxFit)
#         if maxFit == 64:
#             print('done')
#             break
#         elif maxFit > 40:
#             print('done')
#             break
#         population.create_new_generation ()
 

def run_genetic_algorithm():
    population = Population(population_size=50)
    max_generations = 1000
    while population.generation < max_generations:
        population.check_population()
        best_knight, fitness = population.evaluate()
        print("Best solution: ", fitness)
        if fitness == 64:
            print(f"Solution found in generation {population.generation}!")
            return(best_knight.path)
        population.create_new_generation()

movs = run_genetic_algorithm()
animate(movs)

# main()
