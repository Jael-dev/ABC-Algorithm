import os

class Config:
    """
    Configuration class for task allocation system.
    """

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Task Allocation Settings
    MAX_ITERATIONS = 100  # Number of iterations for the ABC algorithm
    COLONY_SIZE = 50      # Number of bees (solutions) in the colony
    LIMIT = 10            # Limit for abandoning solutions

    # Default Task, Robot, and Human Configurations
    DEFAULT_TASK_COUNT = 20
    DEFAULT_ROBOT_COUNT = 5
    DEFAULT_HUMAN_COUNT = 5

    # Logging Settings
    LOGGING_ENABLED = True
    LOG_FILE = os.path.join(BASE_DIR, "logs", "task_allocation.log")

    # Visualization Settings
    DISPLAY_RESULTS = True
