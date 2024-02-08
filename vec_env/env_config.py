import random

class Config:

    N_RSU = 3

    @staticmethod
    def rsu_cpu_capacity():
        return random.uniform(1e10, 15e9)

    @staticmethod
    def n_vehicle():
        return random.randint(8, 10)

    @staticmethod
    def obu_cpu_capacity():
        return random.uniform(1e9, 3e9)

    @staticmethod
    def n_task():
        return random.randint(1, 3)

    @staticmethod
    def task_size():
        return random.randint(10, 60)

    @staticmethod
    def max_task_delay():
        return random.uniform(0.1, 2)

    @staticmethod
    def required_cpu_cycle():
        return random.randint(int(8e7), int(48e7))

    @staticmethod
    def vehicle_position():
        return [random.randint(0, 30), random.randint(0, 1000)]

    @staticmethod
    def v2v_transmission_rate():
        return random.uniform(int(8e7), int(4e8))

    V2V_BANDWIDTH = 0.3
    V2V_NOISE = -70
    MAX_ENERGY_CONSUMPTION = 10
    V2V_TRANSMISSION_POWER = 100
    WEIGHT = 0.65
