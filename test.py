import gym
import numpy as np
from gym.spaces import Box


# Assuming the code is part of a gym environment class
class MyEnvironment(gym.Env):
    def __init__(self):
        # Define the observation space
        self.observation_space = Box(low=np.array([0], dtype=np.float32), high=np.array([100], dtype=np.float32))


# Create an instance of the environment
env = MyEnvironment()

# Sample an observation from the environment
observation = env.observation_space.sample()

print(observation)