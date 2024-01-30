import random
from env_config import Config


class Vehicle:

    def __init__(self, vehicle_id, position, transmission_power, cpu_capacity):
        self.vehicle_id = vehicle_id
        self.position = position
        self.transmission_power = transmission_power
        self.cpu_capacity = cpu_capacity

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