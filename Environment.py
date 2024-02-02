from vec_env.env_element import *
from vec_env.env_config import Config
import numpy as np


class Environment:
    def __init__(self):
        self.n_vehicle = Config.n_vehicle()
        self.n_rsu = Config.N_RSU
        self.vehicles = [Vehicle(vehicle_id=i) for i in range(0, self.n_vehicle)]
        self.rsu = [RSU(rsu_id=i) for i in range(0, self.n_rsu)]
        self.queue_delay = [0] * self.n_vehicle
        self.index_i = 0
        self.index_j = 0
        self.task_scheduler = [0] * self.n_vehicle
        self.transmission_rates = [[0] * self.n_vehicle for _ in range(self.n_vehicle)]
        self.reward = 0
        self.terminate = False
        for i in range(self.n_vehicle):
            for k in range(i + 1, self.n_vehicle):
                rate = Config.v2v_transmission_rate()
                self.transmission_rates[i][k] = rate
                self.transmission_rates[k][i] = rate

    def step(self, action):

        i = self.index_i
        j = self.index_j

        if action == i:
            t_execution = self.vehicles[i].task_queue[j]['required_cpu_cycle']/ self.vehicles[i].cpu_capacity
            t = self.queue_delay[i] + t_execution

            if t <= self.vehicles[i].task_queue[j]['task_delay']:
                self.reward = 1 - (t/self.vehicles[i].task_queue[j]['task_delay'])

            else:
                self.reward = -8 * t/self.vehicles[i].task_queue[j]['task_delay']

            self.queue_delay[i] += self.vehicles[i].task_queue[j]['required_cpu_cycle']/ self.vehicles[i].cpu_capacity

        else:
            k = action
            t_execution = self.vehicles[i].task_queue[j]['required_cpu_cycle'] / self.vehicles[k].cpu_capacity
            t_transmission = self.vehicles[i].task_queue[j]['task_size'] / self.transmission_rates[i][k]
            t = self.queue_delay[k] + t_execution + t_transmission

            if t <= self.vehicles[i].task_queue[j]['task_delay']:
                self.reward = 1 - (t/self.vehicles[i].task_queue[j]['task_delay'])

            else:
                self.reward = -8 * t/self.vehicles[i].task_queue[j]['task_delay']

            self.queue_delay[k] += self.vehicles[i].task_queue[j]['required_cpu_cycle'] / self.vehicles[k].cpu_capacity

        self.task_scheduler[i] = j + 1
        j += 1
        if j >= len(self.vehicles[i].task_queue):
            j = 0
            i += 1

        self.index_i = i
        self.index_j = j

        if self.index_i >= self.n_vehicle:
            self.terminate = True

        state = np.concatenate((self.task_scheduler, self.queue_delay))

        return state, self.reward, self.terminate

    def reset(self):
        self.vehicles = [Vehicle(vehicle_id=i) for i in range(0, self.n_vehicle)]
        self.rsu = [RSU(rsu_id=i) for i in range(0, self.n_rsu)]
        self.queue_delay = [0] * self.n_vehicle
        self.index_i = 0
        self.index_j = 0
        self.task_scheduler = [0] * self.n_vehicle
        self.transmission_rates = [[0] * self.n_vehicle for _ in range(self.n_vehicle)]
        self.reward = 0
        self.terminate = False
        for i in range(self.n_vehicle):
            for k in range(i + 1, self.n_vehicle):
                rate = Config.v2v_transmission_rate()
                self.transmission_rates[i][k] = rate
                self.transmission_rates[k][i] = rate

        state = np.concatenate((self.task_scheduler, self.queue_delay))
        return state










# print(self.queue_delay)
        #
        # for i in self.vehicles:
        #     for j in i.task_queue:
        #         print("vehicle id : " + str(i.vehicle_id))
        #         print(i.cpu_capacity)
        #         print(j)
        #         self.queue_delay[i.vehicle_id] += j['required_cpu_cycle'] / i.cpu_capacity
        #
        # print(self.queue_delay)


# num_vehicles = random.randint(10, 20)
# vehicles = []
#
# for i in range(1, num_vehicles + 1):
#     vehicle = Vehicle(vehicle_id=i)
#     vehicles.append(vehicle)
#
# for vehicle in vehicles:
#     print(f"Vehicle {vehicle.vehicle_id} at position {vehicle.position}:")
#     print(f"Transmission Power: {vehicle.transmission_power}")
#     print(f"CPU Capacity: {vehicle.cpu_capacity}")
#     print("Tasks:")
#     for task in vehicle.task_queue:
#         print(task)
#     print("\n")



