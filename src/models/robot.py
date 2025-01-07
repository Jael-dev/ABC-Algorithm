class Robot:
    def __init__(self, robot_id, capabilities, location=(0, 0), capacity=10):
        """
        Represents a robot capable of performing tasks.
        :param robot_id: Unique identifier for the robot.
        :param capabilities: List of task complexities the robot can handle.
        :param location: Current location of the robot (default: (0, 0)).
        """
        self.robot_id = robot_id
        self.capabilities = capabilities
        self.location = location
        self.capacity = capacity
        self.task_queue = []

    def move_to(self, new_location):
        """
        Updates the robot's location.
        :param new_location: Tuple representing the new location (x, y).
        """
        self.location = new_location

    def __repr__(self):
        return f"Robot({self.robot_id}, Capabilities: {self.capabilities}, Location: {self.location})"
