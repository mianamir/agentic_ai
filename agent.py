import random

class Agent:
    def __init__(self, name):
        self.name = name
        self.perception = None

    def perceive(self, environment):
        self.perception = environment.get_state()
        print(f"{self.name} perceived: {self.perception}")

    def decide(self):
        # Make a decision based on perception
        # For simplicity, we'll randomly choose an action
        action = random.choice(["move_left", "move_right", "move_up", "move_down"])
        print(f"{self.name} decided to: {action}")
        return action

    def act(self, environment, action):
        # Act on the environment
        environment.update_state(action)
        print(f"{self.name} acted: {action}")