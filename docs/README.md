# Task Allocation System

The Task Allocation System is an implementation of an Artificial Bee Colony (ABC) algorithm to optimize the allocation of tasks among humans and robots in a given environment. This project is modular and extensible, allowing you to define tasks, agents, and evaluation criteria flexibly.

---

## Features
- Assign tasks to humans and robots based on their capabilities.
- Optimize task allocation using the Artificial Bee Colony (ABC) algorithm.
- Modular design with extendable components for tasks, agents, and evaluation.
- Unit tests to ensure functionality.

---

## Project Structure
```
ABC-Algorithm/
│
├── src/
│   ├── __init__.py
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── abc_algorithm.py
│   │   └── task_allocation.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py
│   │   ├── robot.py
│   │   ├── human.py
│   │   └── environment.py
│   ├── interface/
│   │   ├── __init__.py
│   │   ├── user_input.py
│   │   └── visualization.py
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── metrics.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_abc_algorithm.py
│   ├── test_models.py
│   └── test_task_allocation.py
├── requirements.txt
├── README.md
└── data/
    └── sample_data.json
```

---

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or later
- Virtual environment (optional, but recommended)

---

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ABC-Algorithm.git
   cd ABC-Algorithm
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv abc_env
   source abc_env/bin/activate  # On Windows: abc_env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

---

## How to Run the Code
1. Prepare your input data (e.g., tasks, robots, and humans) in `data/sample_data.json`:
   ```json
   {
       "tasks": [
           {"task_id": "Task-1", "complexity": 3, "execution_time": 5.0, "dependencies": [], "location": [10, 20]},
           {"task_id": "Task-2", "complexity": 5, "execution_time": 7.5, "dependencies": ["Task-1"], "location": [15, 25]}
       ],
       "robots": [
           {"robot_id": "Robot-1", "capabilities": [3, 4, 5], "location": [0, 0]},
           {"robot_id": "Robot-2", "capabilities": [5, 6], "location": [5, 10]}
       ],
       "humans": [
           {"human_id": "Human-1", "skills": [2, 3, 4]},
           {"human_id": "Human-2", "skills": [5, 6]}
       ]
   }
   ```

2. Run the main script:
   ```bash
   python src/main.py
   ```

---

## How to Test the Code
1. Activate your virtual environment:
   ```bash
   source abc_env/bin/activate  # On Windows: abc_env\Scripts\activate
   ```

2. Install `pytest` (if not already installed):
   ```bash
   pip install pytest
   ```

3. Run all tests:
   ```bash
   pytest tests/
   ```

4. Check for passing results. Example output:
   ```
   ============================= test session starts =============================
   platform darwin -- Python 3.x.x, pytest-8.x.x, pluggy-1.x.x
   collected 16 items

   tests/test_abc_algorithm.py .....
   tests/test_models.py ..........
   tests/test_task_allocation.py ...

   ========================== 16 passed in 1.23s ===========================
   ```

---

## Customization
You can extend or modify the system by:
- Adding new task types in `src/models/task.py`.
- Extending agent capabilities in `src/models/robot.py` and `src/models/human.py`.
- Customizing evaluation metrics in `src/evaluation/metrics.py`.

---

## Troubleshooting
- **`ModuleNotFoundError: No module named 'src'`**:
  Ensure the `PYTHONPATH` includes the project root directory. You can set it temporarily:
  ```bash
  export PYTHONPATH=$(pwd)
  ```

- **`pip` SSL errors**:
  Ensure Python is installed with SSL support. Reinstall Python if necessary.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author
- Brandon


