import random
from vec_env.env_config import Config


class Vehicle:

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.position = Config.vehicle_position()
        self.transmission_power = Config.V2V_TRANSMISSION_POWER
        self.cpu_capacity = Config.obu_cpu_capacity()
        self.task_queue = []
        self.generate_random_tasks()

    def generate_random_tasks(self):
        num_tasks = 1
        for _ in range(num_tasks):
            task = {
                'task_delay': Config.max_task_delay(),
                'required_cpu_cycle': Config.required_cpu_cycle(),
                'task_size': Config.task_size()
            }

            self.task_queue.append(task)

    def reset(self):
        self.position = Config.vehicle_position()
        self.transmission_power = Config.V2V_TRANSMISSION_POWER
        self.cpu_capacity = Config.obu_cpu_capacity()
        self.task_queue = []
        self.generate_random_tasks()


class RSU:
    def __init__(self, rsu_id):
        self.rsu_id = rsu_id
        self.cpu_capacity = Config.rsu_cpu_capacity()

    def reset(self):
        self.cpu_capacity = Config.rsu_cpu_capacity()