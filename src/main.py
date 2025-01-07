from src.models.environment import Environment
from src.algorithms.abc_algorithm import ABCAlgorithm
from src.interface.user_input import get_task_data, get_robot_data, get_human_data
from src.interface.visualization import display_allocation_results, display_best_solution, display_execution_time
from config import Config


def main():
    """
    Main function to run the task allocation system.
    """
    # Initialize tasks, robots, and humans
    print("Initializing environment...")
    tasks = get_task_data()
    robots = get_robot_data()
    humans = get_human_data()

    # Create the environment
    environment = Environment(tasks=tasks, robots=robots, humans=humans)
    print(f"Environment initialized with {len(tasks)} tasks, {len(robots)} robots, and {len(humans)} humans.")

    # Initialize and run the ABC Algorithm
    print("Running the ABC Algorithm...")
    abc_algorithm = ABCAlgorithm(
        environment=environment,
        max_iterations=Config.MAX_ITERATIONS,
        colony_size=Config.COLONY_SIZE,
        limit=Config.LIMIT
    )

    execution_time, best_fitness, best_solution = None, None, None
    try:
        # Execute the algorithm and measure execution time
        import time
        start_time = time.time()
        best_solution, best_fitness = abc_algorithm.run()
        end_time = time.time()
        execution_time = end_time - start_time
    except Exception as e:
        print(f"An error occurred while running the algorithm: {e}")
        return

    # Display results
    print("Displaying results...")
    display_allocation_results({task.task_id: agent for task, agent in zip(tasks, best_solution)})
    display_best_solution(best_solution, best_fitness)
    display_execution_time(execution_time)

if __name__ == "__main__":
    main()
