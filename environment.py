class Environment:
    def __init__(self):
        self.state = "initial_state"
        self.reward = 0

    def update_state(self, action):
        # Update the environment state based on the agent's action
        self.state = f"state_after_{action}"
        self.reward = self.calculate_reward(action)
        print(f"Environment updated to: {self.state} with reward: {self.reward}")

    def get_state(self):
        # Return the current state of the environment
        return self.state

    def calculate_reward(self, action):
        # Calculate reward based on action
        # For simplicity, we'll assign a random reward
        reward = random.randint(-10, 10)
        return reward