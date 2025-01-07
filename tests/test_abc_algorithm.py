import unittest
from src.models.environment import Environment
from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human
from src.algorithms.abc_algorithm import ABCAlgorithm

class TestABCAlgorithm(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task(task_id=f"Task-{i}", complexity=i + 1, execution_time=1.0)
            for i in range(5)
        ]
        self.robots = [
            Robot(robot_id=f"Robot-{i}", capabilities=[1, 2, 3]) for i in range(2)
        ]
        self.humans = [
            Human(human_id=f"Human-{i}", skills=[1, 2]) for i in range(2)
        ]
        self.environment = Environment(tasks=self.tasks, robots=self.robots, humans=self.humans)
        self.abc_algorithm = ABCAlgorithm(
            environment=self.environment, max_iterations=100, colony_size=50, limit=10
        )

    def test_initialize_food_sources(self):
        self.abc_algorithm.initialize_food_sources()
        self.assertEqual(len(self.abc_algorithm.food_sources), 50)
        for solution in self.abc_algorithm.food_sources:
            for agent_id in solution:
                self.assertIn(agent_id, [r.robot_id for r in self.robots] + [h.human_id for h in self.humans])

    def test_employed_bees_phase(self):
        self.abc_algorithm.initialize_food_sources()
        self.abc_algorithm.employed_bees_phase()
        self.assertEqual(len(self.abc_algorithm.fitness), 50)

    def test_run_algorithm(self):
        best_solution, best_fitness = self.abc_algorithm.run()
        self.assertIsNotNone(best_solution)
        self.assertGreaterEqual(best_fitness, 0)

    # Ensure all agent IDs in the solution are valid
        for agent_id in best_solution:
            self.assertIn(agent_id, [r.robot_id for r in self.robots] + [h.human_id for h in self.humans])

    
if __name__ == "__main__":
    unittest.main()
