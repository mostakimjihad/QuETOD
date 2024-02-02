from matplotlib import pyplot as plt
import pandas as pd
from Environment import Environment
from agents.dqn import DQN
import numpy as np

env = Environment()
states = 2 * env.n_vehicle
actions = env.n_vehicle
deep_dqn = DQN(states, actions)

score_record = []
score_record_step = []
count_record = []
count_record_step = []
time_record = []
time_record_step = []
episode_record = []
episode_record_step = []

cost_record = []
cost_record_step = []
for i in range(10):
    score = 0
    state = env.reset()
    done = False
    while not done:
        act = deep_dqn.choose_action(state)
        new_state, reward, done = env.step(act)
        print(f'action reward : {reward}')
        deep_dqn.store_transition(state, act, reward, new_state)
        score += reward
        state = new_state
        if deep_dqn.memory_counter > 2000:
            deep_dqn.learn()
        print('cumaletive reward is： {}'.format(score))

    episode_record.append(i)
    score_record.append(score)

print(episode_record)
print(score_record)
