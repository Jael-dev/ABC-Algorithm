def calculate_fitness(solution, environment):
    """
    Calculate the fitness of a given solution.
    :param solution: A list mapping task IDs to agent IDs.
    :param environment: Environment object containing tasks, robots, and humans.
    :return: Fitness score (higher is better).
    """
    task_allocation = {}

    # Build task allocation from the solution
    for task, agent_id in zip(environment.tasks, solution):
        task_allocation[task.task_id] = agent_id

    fitness = environment.evaluate_fitness(task_allocation)
    return fitness

def evaluate_agent_efficiency(agent, tasks):
    """
    Evaluate the efficiency of an agent in completing assigned tasks.
    :param agent: A Human or Robot object.
    :param tasks: List of tasks assigned to the agent.
    :return: Efficiency score.
    """
    if not tasks:
        return 0

    total_efficiency = 0

    for task in tasks:
        if hasattr(agent, 'capabilities') and task.complexity in agent.capabilities:
            total_efficiency += task.complexity * 0.8  # Higher efficiency for robots
        elif hasattr(agent, 'skills') and task.complexity in agent.skills:
            total_efficiency += task.complexity * 0.5  # Lower efficiency for humans

    workload_penalty = max(0, len(tasks) - getattr(agent, 'capacity', len(tasks)))  # Penalize for exceeding capacity
    return total_efficiency - workload_penalty

def evaluate_task_compatibility(agent, task):
    """
    Evaluate the compatibility between an agent and a task.
    :param agent: A Human or Robot object.
    :param task: A Task object.
    :return: Compatibility score.
    """
    compatibility_score = 0

    if hasattr(agent, 'capabilities') and task.complexity in agent.capabilities:
        compatibility_score += 10  # Robot compatibility
    elif hasattr(agent, 'skills') and task.complexity in agent.skills:
        compatibility_score += 5  # Human compatibility

    if hasattr(agent, 'location') and task.location:
        # Penalize based on distance to the task location (example formula)
        distance = ((agent.location[0] - task.location[0]) ** 2 + (agent.location[1] - task.location[1]) ** 2) ** 0.5
        compatibility_score -= distance * 0.1

    return compatibility_score

def calculate_overall_allocation_fitness(allocation, environment):
    """
    Calculate the overall fitness score of a task allocation.
    :param allocation: Dictionary mapping task IDs to agent IDs.
    :param environment: Environment containing tasks, robots, and humans.
    :return: Overall fitness score.
    """
    fitness = 0

    for task_id, agent_id in allocation.items():
        task = next((t for t in environment.tasks if t.task_id == task_id), None)
        agent = next((r for r in environment.robots if r.robot_id == agent_id), None) or \
                next((h for h in environment.humans if h.human_id == agent_id), None)

        if not task or not agent:
            continue

        fitness += evaluate_task_compatibility(agent, task)
        fitness += evaluate_agent_efficiency(agent, [task])

    return fitness
