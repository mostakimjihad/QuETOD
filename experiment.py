import numpy as np
from matplotlib import pyplot as plt
from Environment import Environment
from agents.dqn import DQN

env = Environment()
states = 2 * env.n_vehicle
actions = env.n_vehicle
deep_dqn = DQN(states, actions)

score_record = []
experience = []
episode_record = []
for i in range(3000):
    score = 0
    state = env.reset()
    done = False
    while not done:
        act = deep_dqn.choose_action(state)
        new_state, reward, done = env.step(act)
        # print(f'action reward : {reward}')
        deep_dqn.store_transition(state, act, reward, new_state)
        score += reward
        state = new_state
        if deep_dqn.memory_counter > 2000:
            deep_dqn.learn()
        # print('cumaletive reward is： {}'.format(score))
    print(score)
    episode_record.append(i)
    experience.append(env.experience/env.n_vehicle)
    score_record.append(score)

# plt.plot(episode_record, score_record, label='Score vs Episode')
# plt.rcParams['font.size'] = '12'
# plt.xlabel('Episode')
# plt.ylabel('Score')
# plt.legend()
# plt.show()
sample_indices = np.random.choice(len(episode_record), 5, replace=False)
sample_episodes = [episode_record[i] for i in sample_indices]
sample_qoe = [experience[i] for i in sample_indices]

plt.errorbar(sample_episodes, sample_qoe, marker ='|',ms = 6, label='QuETOD', yerr = 0.04)
plt.rcParams['font.size'] = '12'
plt.xlabel('Episode')
plt.ylabel('Average QoE')
plt.legend()
plt.show()

