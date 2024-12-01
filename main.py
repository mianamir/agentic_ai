from agent import Agent
from environment import Environment

def main():
    # Initialize the environment
    env = Environment()

    # Initialize the agent
    agent = Agent(name="Agent1")

    # Main loop
    for _ in range(10):  # Run for 10 iterations
        agent.perceive(env)
        action = agent.decide()
        agent.act(env, action)
        env.update_state(action)

if __name__ == "__main__":
    main()