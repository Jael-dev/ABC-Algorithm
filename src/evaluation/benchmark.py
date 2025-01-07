import time
import random
from src.models.task import Task
from src.models.human import Human
from src.models.robot import Robot
from src.models.environment import Environment
from src.abc_algorithm import ABCAlgorithm

class Benchmark:
    def __init__(self, task_count, robot_count, human_count):
        """
        Initialize the benchmark environment.
        :param task_count: Number of tasks to generate.
        :param robot_count: Number of robots to generate.
        :param human_count: Number of humans to generate.
        """
        self.task_count = task_count
        self.robot_count = robot_count
        self.human_count = human_count
        self.environment = None

    def generate_tasks(self):
        """Generate a list of tasks with random complexities and execution times."""
        return [
            Task(
                task_id=f"Task-{i}",
                complexity=random.randint(1, 10),
                execution_time=random.uniform(1.0, 10.0),
                dependencies=[],
                location=(random.randint(0, 100), random.randint(0, 100))
            )
            for i in range(self.task_count)
        ]

    def generate_robots(self):
        """Generate a list of robots with random capabilities."""
        return [
            Robot(
                robot_id=f"Robot-{i}",
                capabilities=[random.randint(1, 10) for _ in range(random.randint(1, 5))],
                location=(random.randint(0, 100), random.randint(0, 100))
            )
            for i in range(self.robot_count)
        ]

    def generate_humans(self):
        """Generate a list of humans with random skills."""
        return [
            Human(
                human_id=f"Human-{i}",
                skills=[random.randint(1, 10) for _ in range(random.randint(1, 5))]
            )
            for i in range(self.human_count)
        ]

    def setup_environment(self):
        """Setup the environment with generated tasks, robots, and humans."""
        tasks = self.generate_tasks()
        robots = self.generate_robots()
        humans = self.generate_humans()
        self.environment = Environment(tasks=tasks, robots=robots, humans=humans)

    def run_benchmark(self, max_iterations=100, colony_size=50, limit=10):
        """
        Run the ABC Algorithm benchmark.
        :param max_iterations: Maximum number of iterations for the algorithm.
        :param colony_size: Size of the bee colony.
        :param limit: Limit for solution abandonment.
        :return: Execution time and best fitness score.
        """
        self.setup_environment()
        abc_algorithm = ABCAlgorithm(
            environment=self.environment,
            max_iterations=max_iterations,
            colony_size=colony_size,
            limit=limit
        )

        start_time = time.time()
        best_solution, best_fitness = abc_algorithm.run()
        end_time = time.time()

        execution_time = end_time - start_time
        return execution_time, best_fitness, best_solution

if __name__ == "__main__":
    # Example benchmark setup
    task_count = 20
    robot_count = 5
    human_count = 5

    benchmark = Benchmark(task_count, robot_count, human_count)
    execution_time, best_fitness, best_solution = benchmark.run_benchmark()

    print(f"Execution Time: {execution_time:.2f} seconds")
    print(f"Best Fitness: {best_fitness}")
    print(f"Best Solution: {best_solution}")
