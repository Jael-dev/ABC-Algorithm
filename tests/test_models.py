import unittest
from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human
from src.models.environment import Environment
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        task = Task(task_id="Task-1", complexity=5, execution_time=2.0, dependencies=["Task-0"], location=(10, 15))
        self.assertEqual(task.task_id, "Task-1")
        self.assertEqual(task.complexity, 5)
        self.assertEqual(task.execution_time, 2.0)
        self.assertEqual(task.dependencies, ["Task-0"])
        self.assertEqual(task.location, (10, 15))

    def test_task_representation(self):
        task = Task(task_id="Task-1", complexity=5, execution_time=2.0)
        self.assertEqual(repr(task), "Task(Task-1, Complexity: 5, Dependencies: [])")

class TestRobotModel(unittest.TestCase):
    def test_robot_creation(self):
        robot = Robot(robot_id="Robot-1", capabilities=[1, 2, 3], location=(5, 5))
        self.assertEqual(robot.robot_id, "Robot-1")
        self.assertEqual(robot.capabilities, [1, 2, 3])
        self.assertEqual(robot.location, (5, 5))

    def test_robot_move_to(self):
        robot = Robot(robot_id="Robot-1", capabilities=[1, 2, 3], location=(0, 0))
        robot.move_to((10, 15))
        self.assertEqual(robot.location, (10, 15))

    def test_robot_representation(self):
        robot = Robot(robot_id="Robot-1", capabilities=[1, 2, 3])
        self.assertEqual(repr(robot), "Robot(Robot-1, Capabilities: [1, 2, 3], Location: (0, 0))")

class TestHumanModel(unittest.TestCase):
    def test_human_creation(self):
        human = Human(human_id="Human-1", skills=[4, 5, 6])
        self.assertEqual(human.human_id, "Human-1")
        self.assertEqual(human.skills, [4, 5, 6])

    def test_human_assign_task(self):
        human = Human(human_id="Human-1", skills=[4, 5, 6])
        task = Task(task_id="Task-1", complexity=4, execution_time=2.0)
        human.assign_task(task)
        self.assertIn(task, human.task_queue)
        self.assertEqual(human.workload, 4)

    def test_human_representation(self):
        human = Human(human_id="Human-1", skills=[4, 5, 6])
        self.assertEqual(repr(human), "Human(Human-1, Skills: [4, 5, 6], Workload: 0)")

class TestEnvironmentModel(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task(task_id=f"Task-{i}", complexity=i + 1, execution_time=1.0)
            for i in range(5)
        ]
        self.robots = [
            Robot(robot_id=f"Robot-{i}", capabilities=[1, 2, 3])
            for i in range(2)
        ]
        self.humans = [
            Human(human_id=f"Human-{i}", skills=[1, 2])
            for i in range(2)
        ]
        self.environment = Environment(tasks=self.tasks, robots=self.robots, humans=self.humans)

    def test_environment_initialization(self):
        self.assertEqual(len(self.environment.tasks), 5)
        self.assertEqual(len(self.environment.robots), 2)
        self.assertEqual(len(self.environment.humans), 2)

    def test_environment_evaluate_fitness(self):
        allocation = {task.task_id: self.robots[0].robot_id for task in self.tasks}
        fitness = self.environment.evaluate_fitness(allocation)
        self.assertGreaterEqual(fitness, 0)

if __name__ == "__main__":
    unittest.main()
