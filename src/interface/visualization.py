def display_allocation_results(results):
    """
    Display the task allocation results in a readable format.
    :param results: Dictionary mapping task IDs to agent IDs.
    """
    print("\nTask Allocation Results:")
    print("--------------------------")
    for task, agent in results.items():
        print(f"Task {task} -> Assigned to Agent {agent}")

def display_best_solution(best_solution, fitness_score):
    """
    Display the best solution and its fitness score.
    :param best_solution: The best solution as a list mapping tasks to agents.
    :param fitness_score: The fitness score of the best solution.
    """
    print("\nBest Solution:")
    print("-----------------")
    print(f"Solution: {best_solution}")
    print(f"Fitness Score: {fitness_score}")

def display_execution_time(execution_time):
    """
    Display the execution time of the algorithm.
    :param execution_time: Time taken to execute the algorithm.
    """
    print("\nExecution Time:")
    print("-----------------")
    print(f"Time: {execution_time:.2f} seconds")
