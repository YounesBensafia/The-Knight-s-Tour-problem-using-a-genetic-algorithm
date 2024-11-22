from Chromosome import Chromosome
import random

class Knight:
    def __init__(self, chromosome=None):
        self.position = (0, 0) 
        self.chromosome = chromosome if chromosome else Chromosome()
        self.path = [self.position]
        self.check_moves()
        self.fitness = 0

    def move_forward(self, direction):
        move_directions = {
            1: (-2, 1), 2: (-1, 2), 3: (1, 2), 4: (2, 1),
            5: (2, -1), 6: (1, -2), 7: (-1, -2), 8: (-2, -1)
        }
    
        dx, dy = move_directions[direction]
        new_position = (self.position[0] + dx, self.position[1] + dy)
        return new_position

    def move_backward(self, direction):
        move_directions = {
            1: (2, -1), 2: (1, -2), 3: (-1, -2), 4: (-2, -1),
            5: (-2, 1), 6: (-1, 2), 7: (1, 2), 8: (2, 1)
        }
        dx, dy = move_directions[direction]
        new_position = (self.position[0] + dx, self.position[1] + dy)
        return new_position

    def check_moves(self):
        for i, move in enumerate(self.chromosome.genes):
            new_position = self.move_forward(move)
            if not self.is_valid_move(new_position):
                self.chromosome.genes[i] = self.get_next_valid_move(i)

    def is_valid_move(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8 and position not in self.path

    def get_next_valid_move(self, i):
        possible_moves = list(range(1, 9))
        random.shuffle(possible_moves)
        for move in possible_moves:
            if self.is_valid_move(self.move_forward(move)):
                return move
        return self.chromosome.genes[i] 

    def evaluate_fitness(self):
        visited = set(self.path)
        self.fitness = len(visited)
        return self.fitness
