from vec_env.env_element import *

num_vehicles = random.randint(10, 20)
vehicles = []

for i in range(1, num_vehicles + 1):
    vehicle = Vehicle(vehicle_id=i)
    vehicles.append(vehicle)

for vehicle in vehicles:
    tasks = vehicle.generate_random_tasks()
    print(f"Vehicle {vehicle.vehicle_id} at position {vehicle.position}:")
    print(f"Transmission Power: {vehicle.transmission_power}")
    print(f"CPU Capacity: {vehicle.cpu_capacity}")
    print("Tasks:")
    for task in tasks:
        print(task)
    print("\n")

