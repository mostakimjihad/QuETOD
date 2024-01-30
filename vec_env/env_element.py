import random
from env_config import Config


class Vehicle:

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.position = Config.po
        self.transmission_power = Config.V2V_TRANSMISSION_POWER
        self.cpu_capacity = Config.OBU_CPU_CAPACITY

    def generate_random_tasks(self, num_tasks: int = Config.N_TASK):
        task_queue = []
        for _ in range(num_tasks):
            task = {
                'task_delay': Config.MAX_TASK_DELAY,
                'required_cpu_cycle': Config.REQUIRED_CPU_CYCLE,
                'task_size': Config.TASK_SIZE
            }

            task_queue.append(task)

        return task_queue


class RSU:
    def __init__(self, rsu_id, position, cpu_capacity):
        self.rsu_id = rsu_id
        self.position = position
        self.cpu_capacity = cpu_capacity