import random


class Config(object):
    N_RSU = 3
    RSU_CPU_CAPACITY = random.uniform(10, 15)
    N_VEHICLE = random.randint(20, 40)
    OBU_CPU_CAPACITY = random.uniform(1, 3)
    N_TASK = random.randint(1, 3)
    V2V_BANDWIDTH = 0.3
    TASK_SIZE = random.randint(10, 60)
    V2V_NOISE = -70
    MAX_TASK_DELAY = random.uniform(0.1, 2)
    MAX_ENERGY_CONSUMPTION = 10
    REQUIRED_CPU_CYCLE = 800
    V2V_TRANSMISSION_POWER = 100

    WEIGHT = 0.65

    VEHICLE_POSITION = [random.randint(0, 30), random.randint(0, 1000)]


