# The-Knight-s-Tour-problem-using-a-genetic-algorithm

<img height="200" alt="knights" src="https://github.com/user-attachments/assets/5fac0311-72cb-4485-89fe-19903a15f108" width="100%"/>



The knight can move to the square marked in red and then repeat the process on the new square.
A **knight's tour** is a sequence of moves where the knight visits every square on the chessboard exactly once.

---

## Objective

The goal of this assignment is to solve the knight's tour problem using a **genetic algorithm** by creating the following classes:

---

## 1. Chromosome Class

In the knight's tour problem, the **moves made by the knight** represent the genes of the chromosome.

**Attributes:**

* `genes`: an array of length 63 representing the knight's moves. Each gene corresponds to one of the 8 possible moves.

**Functions:**

* `__init__(genes)`:
  Creates a new chromosome. If no genes are provided (as in the initial population), it generates a random set of genes.

* `crossover(partner)`:
  Combines genes from this chromosome and another (`partner`) using **single-point crossover** to create new offspring.

* `mutation()`:
  Introduces mutations by randomly changing some genes with a certain probability, helping the genetic algorithm explore new moves.

---

## 2. Knight Class

Each knight stores the following:

* `position`: coordinates `(x, y)` for the knight's current position.
* `chromosome`: sequence of moves taken by the knight.
* `path`: list of knight's positions after applying moves from the chromosome.
* `fitness`: fitness value, with a maximum of 64 (total squares on the chessboard).

**Functions:**

* `__init__(chromosome)`:
  Creates a new knight. If no chromosome is provided, generates a new one. Sets the initial position to `(0, 0)`, fitness to 0, and saves the initial position in `path`.

* `move_forward(direction)`:
  Moves the knight in one of 8 directions:
![image](https://github.com/user-attachments/assets/f1114825-b354-4484-a29f-92aecb3727f5)
  1. up-right
  2. right-up
  3. right-down
  4. down-right
  5. down-left
  6. left-down
  7. left-up
  8. up-left
     Computes the new position after the move.

* `move_backward(direction)`:
  Reverts the knight’s position if the move was illegal.

* `check_moves()`:
  Checks validity of each move in the chromosome. A move is invalid if it places the knight outside the board or on a previously visited square.
  If invalid, cancels the move using `move_backward()` and tests other moves by cycling forward or backward.
  The cycling direction is chosen randomly at the start and remains consistent for the entire chromosome.

  * **Forward cycle example:** For current move `4 (down-right)`, the order to test is:
    5 (down-left), 6 (left-down), 7 (left-up), 8 (up-left), 1 (up-right), 2 (right-up), 3 (right-down)
  * **Backward cycle example:** For current move `4 (down-right)`, the order to test is:
    3 (right-down), 2 (right-up), 1 (up-right), 8 (up-left), 7 (left-up), 6 (left-down), 5 (down-left)
    If no valid move is found, the last move is retained.

* `evaluate_fitness()`:
  Calculates the fitness by iterating through the knight’s path and counting valid visited squares until an invalid move is encountered.
  Fitness is 64 if all squares are visited.

---

## 3. Population Class

Represents a group of knights.

**Attributes:**

* `population_size`: e.g., 50.
* `generation`: number of generations (initially 1).
* `knights`: list of knights in the population.

**Functions:**

* `__init__(population_size)`:
  Initializes the population with knights and sets generation to 1.

* `check_population()`:
  Loops through all knights and checks their moves’ validity using `check_moves()`.

* `evaluate()`:
  Evaluates the fitness of every knight using `evaluate_fitness()`. Returns the best knight and its fitness.

* `tournament_selection(size)`:
  Selects parents for crossover using tournament selection with sample size `n` (e.g., 3).
  Randomly samples `n` knights and selects the two best based on fitness.

* `create_new_generation()`:
  Creates a new population of the same size. For each pair of offspring:

  * Select parents with `tournament_selection(size)`.
  * Generate offspring via `crossover(partner)` on their chromosomes.
  * Apply `mutation()` to offspring chromosomes.
  * Increment generation count.

---

## 4. Main Function

Runs the genetic algorithm and displays the optimal solution through a graphical interface.



![image](https://github.com/user-attachments/assets/74bd702d-0723-4837-bffb-39daf31d3bd9)



![image](https://github.com/user-attachments/assets/13441d65-eca6-4279-996f-6670c5c12bb6)



https://github.com/user-attachments/assets/76e234a3-969d-49f0-8558-447ba2233882




