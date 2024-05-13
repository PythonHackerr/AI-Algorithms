import numpy as np

class Agent:
    def __init__(self, lr, gamma, observation_space, action_space):
        self.q_table = np.zeros((observation_space, action_space))
        self.lr = lr
        self.gamma = gamma

    def pick_best_action(self, state):
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        prev_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        self.q_table[state, action] = prev_value + self.lr * (reward + self.gamma * next_max - prev_value)

