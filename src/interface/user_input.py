from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human

def get_task_data():
    """
    Initialize and return a list of Task instances based on user input or predefined configurations.
    :return: List of Task objects.
    """
    task_count = int(input("Enter the number of tasks: "))
    tasks = []

    for i in range(task_count):
        task_id = f"Task-{i+1}"
        complexity = int(input(f"Enter complexity for {task_id} (1-10): "))
        execution_time = float(input(f"Enter execution time for {task_id} (in seconds): "))
        location = (
            int(input(f"Enter x-coordinate for {task_id}: ")),
            int(input(f"Enter y-coordinate for {task_id}: "))
        )
        tasks.append(Task(task_id=task_id, complexity=complexity, execution_time=execution_time, location=location))

    return tasks

def get_robot_data():
    """
    Initialize and return a list of Robot instances based on user input or predefined configurations.
    :return: List of Robot objects.
    """
    robot_count = int(input("Enter the number of robots: "))
    robots = []

    for i in range(robot_count):
        robot_id = f"Robot-{i+1}"
        capability_count = int(input(f"Enter the number of capabilities for {robot_id}: "))
        capabilities = [
            int(input(f"Enter capability {j+1} for {robot_id} (1-10): "))
            for j in range(capability_count)
        ]
        location = (
            int(input(f"Enter x-coordinate for {robot_id}: ")),
            int(input(f"Enter y-coordinate for {robot_id}: "))
        )
        robots.append(Robot(robot_id=robot_id, capabilities=capabilities, location=location))

    return robots

def get_human_data():
    """
    Initialize and return a list of Human instances based on user input or predefined configurations.
    :return: List of Human objects.
    """
    human_count = int(input("Enter the number of humans: "))
    humans = []

    for i in range(human_count):
        human_id = f"Human-{i+1}"
        skill_count = int(input(f"Enter the number of skills for {human_id}: "))
        skills = [
            int(input(f"Enter skill {j+1} for {human_id} (1-10): "))
            for j in range(skill_count)
        ]
        humans.append(Human(human_id=human_id, skills=skills))

    return humans
