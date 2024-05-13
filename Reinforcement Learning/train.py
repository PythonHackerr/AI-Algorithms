import gym
import random
import numpy as np
from agent import Agent

def train_agent(agent, env, episodes, epsilon):
    timesteps_per_episode = []

    for ep in range(episodes):
        state = env.reset()
        steps = 0
        max_steps = 100
        finished = False
        while (not finished and steps < max_steps):
            if random.uniform(0, 1) > epsilon:  # Exploit
                action = agent.pick_best_action(state)
            else:  # Explore
                action = env.action_space.sample()

            next_state, reward, finished, info = env.step(action)
            agent.update_q_table(state, action, reward, next_state)

            state = next_state
            steps += 1

        timesteps_per_episode.append(steps)

    return agent, timesteps_per_episode


def test_agent(agent, env, episodes):
    timesteps_per_episode = []

    for ep in range(episodes):
        state = env.reset()
        steps = 0
        finished = False
        max_steps = 100
        while (not finished and steps < max_steps):
            action = agent.pick_best_action(state)

            next_state, reward, finished, info = env.step(action)

            state = next_state
            steps += 1

        timesteps_per_episode.append(steps)
        
    return sum(timesteps_per_episode) / len(timesteps_per_episode)


if __name__ == '__main__':
    env = gym.make("Taxi-v2").env
    lr = 0.1
    gamma = 0.6
    agent = Agent(lr, gamma, env.observation_space.n, env.action_space.n)
    agent, _ = train_agent(agent, env, 10000, 0.1)
    timesteps_per_episode = test_agent(agent, env, 10)
    
    print(f'Avg steps to complete episode: {np.array(timesteps_per_episode).mean()}')
