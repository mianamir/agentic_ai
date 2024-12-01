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
        agent.decide()
        agent.act(env)
        env.update_state(agent)

if __name__ == "__main__":
    main()