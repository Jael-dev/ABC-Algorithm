class Task:
    def __init__(self, task_id, complexity, execution_time, dependencies=[], location=None):
        """
        Represents a task in the system.
        :param task_id: Unique identifier for the task.
        :param complexity: Complexity level of the task.
        :param execution_time: Estimated execution time for the task.
        :param dependencies: List of task IDs that must be completed before this task.
        :param location: (Optional) Tuple representing the task location (x, y).
        """
        self.task_id = task_id
        self.complexity = complexity
        self.execution_time = execution_time
        self.dependencies = dependencies
        self.location = location

    def __repr__(self):
        return f"Task({self.task_id}, Complexity: {self.complexity}, Dependencies: {self.dependencies})"
