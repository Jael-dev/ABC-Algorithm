import streamlit as st
import random
from src.models.task import Task
from src.models.robot import Robot
from src.models.human import Human
from src.models.environment import Environment
from src.algorithms.abc_algorithm import ABCAlgorithm

st.title("Task Allocation System")

# Initialize session state for tasks, robots, and humans
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "robots" not in st.session_state:
    st.session_state.robots = []
if "humans" not in st.session_state:
    st.session_state.humans = []
if "allocation_results" not in st.session_state:
    st.session_state.allocation_results = None

# Predefined skills and capabilities
if "skills" not in st.session_state:
    st.session_state.skills = [
        {"id": f"Skill-{i+1}", "name": f"Skill-{i+1}"} for i in range(10)
    ]
if "capabilities" not in st.session_state:
    st.session_state.capabilities = [
        {"id": f"Capability-{i+1}", "name": f"Capability-{i+1}"} for i in range(10)
    ]

# Add tasks
st.header("Add Tasks")
task_id = f"Task-{len(st.session_state.tasks) + 1}"
complexity = st.number_input("Complexity", min_value=1, step=1)
st.write(f"You are adding Task: {task_id}")
if st.button("Add Task"):
    st.session_state.tasks.append(Task(task_id=task_id, complexity=complexity, execution_time=1.0))
    st.success(f"Task {task_id} added!")

# Add robots
st.header("Add Robots")
robot_id = f"Robot-{len(st.session_state.robots) + 1}"
st.write(f"You are adding Robot: {robot_id}")
selected_capabilities = st.multiselect(
    "Select Capabilities",
    options=[cap["name"] for cap in st.session_state.capabilities],
    key="robot_capabilities"
)
if st.button("Add Robot"):
    try:
        capability_indices = [int(cap.split('-')[1]) for cap in selected_capabilities]
        capabilities_list = [int(index) for index in capability_indices]
        st.session_state.robots.append(Robot(robot_id=robot_id, capabilities=capabilities_list))
        st.success(f"Robot {robot_id} added!")
        st.session_state.robot_capabilities = []  # Clear selected capabilities
    except ValueError:
        st.error("Please select valid capabilities from the dropdown.")

# Add humans
st.header("Add Humans")
human_id = f"Human-{len(st.session_state.humans) + 1}"
st.write(f"You are adding Human: {human_id}")
selected_skills = st.multiselect(
    "Select Skills",
    options=[skill["name"] for skill in st.session_state.skills],
    key="human_skills"
)
if st.button("Add Human"):
    try:
        skill_indices = [int(skill.split('-')[1]) for skill in selected_skills]
        skills_list = [int(index) for index in skill_indices]
        st.session_state.humans.append(Human(human_id=human_id, skills=skills_list))
        st.success(f"Human {human_id} added!")
        st.session_state.human_skills = []  # Clear selected skills
    except ValueError:
        st.error("Please select valid skills from the dropdown.")

# Run allocation
if st.button("Run Allocation"):
    if not st.session_state.tasks or not st.session_state.robots or not st.session_state.humans:
        st.error("Please add at least one Task, one Robot, and one Human.")
    else:
        environment = Environment(
            tasks=st.session_state.tasks,
            robots=st.session_state.robots,
            humans=st.session_state.humans,
        )
        abc_algorithm = ABCAlgorithm(
            environment=environment, max_iterations=100, colony_size=50, limit=10
        )
        best_solution, best_fitness = abc_algorithm.run()
        st.session_state.allocation_results = {
            "best_fitness": best_fitness,
            "allocations": [
                {"task_id": task.task_id, "agent": agent}
                for task, agent in zip(st.session_state.tasks, best_solution)
            ]
        }
        st.success("Task allocation completed!")

# Dashboard
st.header("Dashboard")

# Show list of tasks
st.subheader("Tasks")
if st.session_state.tasks:
    st.markdown("### Task List")
    for task in st.session_state.tasks:
        st.markdown(f"**Task ID:** {task.task_id}, **Complexity:** {task.complexity}")
else:
    st.markdown("_No tasks added yet._")

# Show list of robots
st.subheader("Robots")
if st.session_state.robots:
    st.markdown("### Robot List")
    for robot in st.session_state.robots:
        st.markdown(f"**Robot ID:** {robot.robot_id}, **Capabilities:** {robot.capabilities}")
else:
    st.markdown("_No robots added yet._")

# Show list of humans
st.subheader("Humans")
if st.session_state.humans:
    st.markdown("### Human List")
    for human in st.session_state.humans:
        st.markdown(f"**Human ID:** {human.human_id}, **Skills:** {human.skills}")
else:
    st.markdown("_No humans added yet._")

# Show allocation results
st.subheader("Task Allocation Results")
if st.session_state.allocation_results:
    st.markdown("### Allocation Results")
    st.markdown(f"**Best Fitness:** {st.session_state.allocation_results['best_fitness']}")
    for allocation in st.session_state.allocation_results["allocations"]:
        st.markdown(f"**Task {allocation['task_id']} -> Assigned to Agent {allocation['agent']}**")
else:
    st.markdown("_No allocations have been run yet._")
