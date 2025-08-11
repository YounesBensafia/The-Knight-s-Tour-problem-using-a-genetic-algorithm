from population import Population
from animation import animate
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

population = config["population_size"]
max_generations = config["max_generations"]
fitness_target = config["fitness_target"]

def run_genetic_algorithm():
    population = Population(population_size=population)
    while population.generation < max_generations:
        population.check_population()
        best_knight, fitness = population.evaluate()
        print("Best solution: ", fitness)
        if fitness == fitness_target:
            print(f"Solution found in generation {population.generation}!")
            return(best_knight.path)
        population.create_new_generation()


def run():
    population_size = 50
    population = Population(population_size)
    while True:
        population.check_population()
        bestSolution, maxFit= population.evaluate( )
        print("Best solution: ", maxFit)
        if maxFit == 64:
            print('done')
            break
        elif maxFit > 40:
            print('done')
            break
        population.create_new_generation()

if __name__ == "__main__":
    run()
    movs = run_genetic_algorithm()
    animate(movs)

