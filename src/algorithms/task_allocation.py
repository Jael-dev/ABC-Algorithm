from src.models.task import Task
from src.models.human import Human
from src.models.robot import Robot

class TaskAllocator:
    def __init__(self, tasks, agents):
        """
        Initialize the Task Allocator.
        :param tasks: List of Task objects.
        :param agents: List of Human and Robot objects.
        """
        self.tasks = tasks
        self.agents = {
            agent.robot_id if isinstance(agent, Robot) else agent.human_id: agent
            for agent in agents
        }

    def allocate_tasks(self, solution):
        """
        Allocate tasks to agents based on the solution.
        :param solution: List where each element is an agent ID assigned to a task.
        :return: Dictionary of agent IDs with their assigned tasks.
        """
        allocation = {agent_id: [] for agent_id in self.agents.keys()}

        for task, agent_id in zip(self.tasks, solution):
            if agent_id in allocation:
                allocation[agent_id].append(task)
            else:
                raise ValueError(f"Invalid agent ID in solution: {agent_id}")

        return allocation

    def evaluate_allocation(self, allocation):
        """Evaluate the quality of a task allocation."""
        total_score = 0
        for agent_id, assigned_tasks in allocation.items():
            agent = self.agents[agent_id]
            agent_score = self.calculate_agent_score(agent, assigned_tasks)
            total_score += max(agent_score, 0)  # Ensure score doesn't go below 0
        return total_score


    def calculate_agent_score(self, agent, tasks):
        """Calculate a performance score for an agent based on assigned tasks."""
        task_scores = [
            self.task_compatibility(agent, task) for task in tasks
        ]
        # Remove penalty if agent capacity is not defined
        if hasattr(agent, "capacity"):
            workload_penalty = max(0, len(tasks) - agent.capacity)  # Penalize if over capacity
        else:
            workload_penalty = 0

        return sum(task_scores) - workload_penalty

    
    def task_compatibility(self, agent, task):
        if isinstance(agent, Human):
        # Human compatibility: skill level vs task complexity
            compatibility_score = max(0, max(agent.skills) - task.complexity)
            return compatibility_score
        elif isinstance(agent, Robot):
        # Robot compatibility: task complexity within robot's capabilities
            compatibility_score = 10 if task.complexity in agent.capabilities else 0
            return compatibility_score
        else:
            raise ValueError(f"Unknown agent type: {type(agent)}")


    