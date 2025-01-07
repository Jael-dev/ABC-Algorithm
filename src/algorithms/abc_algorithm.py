import random
import numpy as np
from src.models.task import Task
from src.models.human import Human
from src.models.robot import Robot
from src.models.environment import Environment
from src.evaluation.metrics import calculate_fitness

class ABCAlgorithm:
    def __init__(self, environment, max_iterations=100, colony_size=50, limit=10):
        """
        Initialize the ABC algorithm.
        :param environment: Environment object containing tasks, robots, and humans.
        :param max_iterations: Maximum number of iterations to run the algorithm.
        :param colony_size: Total size of the bee colony.
        :param limit: Limit for abandonment of solutions.
        """
        self.environment = environment
        self.tasks = environment.tasks
        self.agents = environment.robots + environment.humans
        self.max_iterations = max_iterations
        self.colony_size = colony_size
        self.limit = limit
        self.food_sources = []  # Each solution maps tasks to agents
        self.fitness = []  # Fitness scores for each solution
        self.trial = []  # Trial counters for each solution

    
    def initialize_food_sources(self):
        """Generate initial random solutions."""
        self.food_sources = [
            [
                agent.robot_id if isinstance(agent := random.choice(self.agents), Robot) else agent.human_id
                for _ in self.tasks
            ]
            for _ in range(self.colony_size)
        ]
        self.fitness = [
            calculate_fitness(solution, self.environment) for solution in self.food_sources
        ]
        self.trial = [0] * self.colony_size

        

    def employed_bees_phase(self):
        """Modify food sources in the employed bee phase."""
        for i in range(self.colony_size):
            new_solution = self.mutate_solution(self.food_sources[i])
            new_fitness = calculate_fitness(new_solution, self.environment)

            # Greedy selection
            if new_fitness > self.fitness[i]:
                self.food_sources[i] = new_solution
                self.fitness[i] = new_fitness
                self.trial[i] = 0
            else:
                self.trial[i] += 1

    def onlooker_bees_phase(self):
        """Generate new solutions for onlooker bees based on fitness probabilities."""
        fitness_probabilities = [f / sum(self.fitness) for f in self.fitness]
        for _ in range(self.colony_size):
            selected_index = self.select_solution(fitness_probabilities)
            new_solution = self.mutate_solution(self.food_sources[selected_index])
            new_fitness = calculate_fitness(new_solution, self.environment)

            # Greedy selection
            if new_fitness > self.fitness[selected_index]:
                self.food_sources[selected_index] = new_solution
                self.fitness[selected_index] = new_fitness
                self.trial[selected_index] = 0
            else:
                self.trial[selected_index] += 1

    def scout_bees_phase(self):
        """Replace abandoned solutions with new random solutions."""
        for i in range(self.colony_size):
            if self.trial[i] > self.limit:
                # Generate a new random solution
                self.food_sources[i] = [
                    agent.robot_id if isinstance(agent := random.choice(self.agents), Robot) else agent.human_id
                    for _ in self.tasks
            ]
                # Recalculate fitness for the new solution
                self.fitness[i] = calculate_fitness(self.food_sources[i], self.environment)
                self.trial[i] = 0


    def mutate_solution(self, solution):
        """Generate a new solution by mutating the current one."""
        new_solution = solution.copy()
        task_index = random.randint(0, len(solution) - 1)
        agent = random.choice(self.agents)
        new_solution[task_index] = (
            agent.robot_id if isinstance(agent, Robot) else agent.human_id
        )
        return new_solution


    def select_solution(self, probabilities):
        """Select a solution based on roulette wheel selection."""
        rand = random.random()
        cumulative = 0
        for i, prob in enumerate(probabilities):
            cumulative += prob
            if rand <= cumulative:
                return i
        return len(probabilities) - 1

    def run(self):
        """Run the ABC algorithm."""
        self.initialize_food_sources()

        for iteration in range(self.max_iterations):
            self.employed_bees_phase()
            self.onlooker_bees_phase()
            self.scout_bees_phase()

            # Debug or logging
            best_solution_index = np.argmax(self.fitness)
            print(f"Iteration {iteration + 1}: Best fitness = {self.fitness[best_solution_index]}")

        # Return the best solution
        best_solution_index = np.argmax(self.fitness)
        return self.food_sources[best_solution_index], self.fitness[best_solution_index]
