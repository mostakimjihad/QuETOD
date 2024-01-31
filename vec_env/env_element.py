import random
from vec_env.env_config import Config


class Vehicle:

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.position = Config.VEHICLE_POSITION
        self.transmission_power = Config.V2V_TRANSMISSION_POWER
        self.cpu_capacity = Config.OBU_CPU_CAPACITY
        self.task_queue = []
        self.generate_random_tasks()

    def generate_random_tasks(self):
        num_tasks = Config.N_TASK
        for _ in range(num_tasks):
            task = {
                'task_delay': Config.MAX_TASK_DELAY,
                'required_cpu_cycle': Config.REQUIRED_CPU_CYCLE,
                'task_size': Config.TASK_SIZE
            }

            self.task_queue.append(task)

    def reset(self):
        self.position = Config.VEHICLE_POSITION
        self.transmission_power = Config.V2V_TRANSMISSION_POWER
        self.cpu_capacity = Config.OBU_CPU_CAPACITY
        self.task_queue = []
        self.generate_random_tasks()




class RSU:
    def __init__(self, rsu_id, position):
        self.rsu_id = rsu_id
        self.position = position
        self.cpu_capacity = Config.RSU_CPU_CAPACITY

    def reset(self):
        self.cpu_capacity = Config.RSU_CPU_CAPACITY