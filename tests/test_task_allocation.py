import unittest
from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human
from src.models.environment import Environment
from src.algorithms.task_allocation import TaskAllocator

class TestTaskAllocator(unittest.TestCase):
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
        self.allocator = TaskAllocator(tasks=self.tasks, agents=self.robots + self.humans)

    def test_task_allocation(self):
        solution = [
            self.robots[0].robot_id if i % 2 == 0 else self.humans[0].human_id
            for i in range(len(self.tasks))
        ]
        allocation = self.allocator.allocate_tasks(solution)
        for agent_id, assigned_tasks in allocation.items():
            self.assertIn(agent_id, [r.robot_id for r in self.robots] + [h.human_id for h in self.humans])
            for task in assigned_tasks:
                self.assertIn(task, self.tasks)

    def test_evaluate_allocation(self):
        solution = [
            self.robots[0].robot_id if i % 2 == 0 else self.humans[0].human_id
            for i in range(len(self.tasks))
    ]
        allocation = self.allocator.allocate_tasks(solution)
        score = self.allocator.evaluate_allocation(allocation)
        self.assertIsInstance(score, (int, float))
        self.assertGreaterEqual(score, 0)

    def test_calculate_agent_score(self):
        agent = self.robots[0]
        tasks = self.tasks[:2]
        score = self.allocator.calculate_agent_score(agent, tasks)
        self.assertIsInstance(score, (int, float))
        self.assertGreaterEqual(score, 0)

if __name__ == "__main__":
    unittest.main()
