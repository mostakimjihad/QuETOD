import random


class Vehicle:
    def __init__(self, vehicle_id, position, transmission_power, cpu_capacity):
        self.vehicle_id = vehicle_id
        self.position = position
        self.transmission_power = transmission_power
        self.cpu_capacity = cpu_capacity

    def generate_random_tasks(self, num_tasks: int = 5):

        tasks = []
        for _ in range(num_tasks):
            task_delay = random.randint(1, 10)  # Maximum task delay
            required_cpu_cycle = random.randint(1, 10)
            data_size = random.randint(10, 100)

            task = {
                'task_delay': task_delay,
                'required_cpu_cycle': required_cpu_cycle,
                'data_size': data_size
            }

            tasks.append(task)

        return tasks


# Generate a random number of vehicles (between 10 and 20)
num_vehicles = random.randint(10, 20)
vehicles = []

for i in range(1, num_vehicles + 1):
    vehicle = Vehicle(vehicle_id=i, position=[random.uniform(0, 100), random.uniform(0, 100)],
                      transmission_power=random.uniform(98, 100), cpu_capacity=random.randint(1, 3))
    vehicles.append(vehicle)

# Display information about the randomly generated vehicles and their tasks
for vehicle in vehicles:
    tasks = vehicle.generate_random_tasks()
    print(f"Vehicle {vehicle.vehicle_id} at position {vehicle.position}:")
    print(f"Transmission Power: {vehicle.transmission_power}")
    print(f"CPU Capacity: {vehicle.cpu_capacity}")
    print("Tasks:")
    for task in tasks:
        print(task)
    print("\n")
