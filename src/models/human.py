class Human:
    def __init__(self, human_id, skills, capacity=5):
        """
        Represents a human worker who can perform tasks.
        :param human_id: Unique identifier for the human.
        :param skills: List of task complexities the human can handle.
        """
        self.human_id = human_id
        self.skills = skills
        self.workload = 0
        self.capacity = capacity
        self.task_queue = []

    def assign_task(self, task):
        """
        Assigns a task to the human.
        :param task: Task object to assign.
        """
        self.task_queue.append(task)
        self.workload += task.complexity

    def __repr__(self):
        return f"Human({self.human_id}, Skills: {self.skills}, Workload: {self.workload})"
