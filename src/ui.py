import streamlit as st
from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human
from src.models.environment import Environment
from src.algorithms.abc_algorithm import ABCAlgorithm

st.title("Task Allocation System")

tasks = []
robots = []
humans = []

# Add tasks
st.header("Add Tasks")
task_id = st.text_input("Task ID")
complexity = st.number_input("Complexity", min_value=1, step=1)
if st.button("Add Task"):
    tasks.append(Task(task_id=task_id, complexity=complexity, execution_time=1.0))
    st.success(f"Task {task_id} added!")

# Add robots
st.header("Add Robots")
robot_id = st.text_input("Robot ID")
capabilities = st.text_input("Capabilities (comma-separated)")
if st.button("Add Robot"):
    robot_capabilities = list(map(int, capabilities.split(",")))
    robots.append(Robot(robot_id=robot_id, capabilities=robot_capabilities))
    st.success(f"Robot {robot_id} added!")

# Add humans
st.header("Add Humans")
human_id = st.text_input("Human ID")
skills = st.text_input("Skills (comma-separated)")
if st.button("Add Human"):
    human_skills = list(map(int, skills.split(",")))
    humans.append(Human(human_id=human_id, skills=human_skills))
    st.success(f"Human {human_id} added!")

# Run allocation
if st.button("Run Allocation"):
    if not tasks or not robots or not humans:
        st.error("Please add at least one Task, one Robot, and one Human.")
    else:
        environment = Environment(tasks=tasks, robots=robots, humans=humans)
        abc_algorithm = ABCAlgorithm(environment=environment, max_iterations=100, colony_size=50, limit=10)
        best_solution, best_fitness = abc_algorithm.run()

        st.write(f"Best Fitness: {best_fitness}")
        st.write("Task Allocation Results:")
        for task, agent in zip(tasks, best_solution):
            st.write(f"Task {task.task_id} -> Assigned to Agent {agent}")
