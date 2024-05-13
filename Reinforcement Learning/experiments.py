import gym
import pandas as pd
from train import train_agent, test_agent
import matplotlib.pyplot as plt
from agent import Agent
import numpy as np

env = gym.make("Taxi-v2").env

#lrs_gammas_vals = [(0.01, 0.1), (0.1, 0.6), (1, 0.9), (0.01, 0.9), (1, 0.1)]
lrs_gammas_vals = [(0.2, 0.2), (0.2, 0.8), (0.8, 0.2), (0.8, 0.8)]
epsilon = 0.1
training_episodes = 2000
episodes_step = 50

results = []
results_sd = []

repeats = 3
test_episodes = 20

for lr, gamma in lrs_gammas_vals:
    timesteps_avg = []
    timesteps_sd = []
    timesteps_aaaa = []
    for i in range(repeats):
        timesteps = []
        for episodes in range(training_episodes):
            if (episodes % episodes_step != 0):
                continue
            agent = Agent(lr, gamma, env.observation_space.n, env.action_space.n)
            agent, _ = train_agent(agent, env, episodes, epsilon)
            timesteps_taken = test_agent(agent, env, test_episodes)
            timesteps.append(timesteps_taken)
        if (len(timesteps_avg) == 0):
            timesteps_avg = timesteps
        else:
            for i in range(len(timesteps_avg)):
                timesteps_avg[i] += timesteps[i]
        timesteps_aaaa.append(timesteps)
    for i in range(len(timesteps_avg)):
        timesteps_avg[i] /= repeats
        timesteps_sd.append(np.std([ts[i] for ts in timesteps_aaaa]))
    results.append({'learning_rate' : lr, 'gamma' : gamma, 'timesteps' : timesteps_avg, 'timesteps_sd' : timesteps_sd})



plot_names = []
for result in results:
    plt.plot(list(range(1*episodes_step, (len(result['timesteps'])+1)*episodes_step, episodes_step)), result['timesteps'])
    plot_names.append(f"lr :{result['learning_rate']}; gamma :{result['gamma']}")


plt.legend(plot_names, loc ="lower right")
plt.xlabel("Episodes")
plt.ylabel("Timesteps")
plt.title("Influence of hyperparameters learning_rate and gamma (epsilon = 0.1)")
plt.show()

for result in results:
    #plt.errorbar(list(np.linspace(1, len(result['timesteps'])+1,len(result['timesteps'][::episodes_step]))), 
    plt.errorbar(list(range(1*episodes_step, (len(result['timesteps'])+1) * episodes_step, episodes_step)), 
        result['timesteps'], 
        yerr=result['timesteps_sd'], 
        marker="o", 
        linestyle="none")
    plot_names = [f"lr :{result['learning_rate']}; gamma :{result['gamma']}"]
    plt.legend(plot_names, loc ="lower right")
    plt.title(f"Standard deviation")
    plt.xlabel("Episodes")
    plt.ylabel("Timesteps")
    plt.show()
