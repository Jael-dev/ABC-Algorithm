class Environment:
    def __init__(self, tasks, robots, humans):
        """
        Represents the environment containing tasks, robots, and humans.
        :param tasks: List of Task objects.
        :param robots: List of Robot objects.
        :param humans: List of Human objects.
        """
        self.tasks = tasks
        self.robots = robots
        self.humans = humans
        self.allocations = {}  # task_id -> agent_id

    def evaluate_fitness(self, allocation):
        """
        Evaluates the fitness of a task allocation.
        :param allocation: Dictionary mapping task_id to agent_id.
        :return: Fitness score (higher is better).
        """
        fitness = 0
        for task_id, agent_id in allocation.items():
            task = next((t for t in self.tasks if t.task_id == task_id), None)
            agent = None

            # Find the agent (robot or human)
            agent = next((r for r in self.robots if r.robot_id == agent_id), None)
            if not agent:
                agent = next((h for h in self.humans if h.human_id == agent_id), None)

            if not task or not agent:
                continue

            # Fitness criteria: compatibility, workload balance, etc.
            if hasattr(agent, "capabilities") and task.complexity in agent.capabilities:
                fitness += 10  # Task is compatible with the agent's capabilities.
            if hasattr(agent, "skills") and task.complexity in agent.skills:
                fitness += 10
            fitness -= len(agent.task_queue)  # Penalize overloaded agents.

        return fitness

    def __repr__(self):
        return f"Environment(Tasks: {len(self.tasks)}, Robots: {len(self.robots)}, Humans: {len(self.humans)})"
