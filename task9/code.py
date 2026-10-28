# Case Study 59: Campus Transport Allocation

routes = ["Route A", "Route B", "Route C"]
passengers = [120, 85, 150]
capacity = 50

total_buses = 0
unserved = 0

for i in range(len(routes)):
    buses = passengers[i] // capacity

    if passengers[i] % capacity != 0:
        buses += 1

    available_seats = buses * capacity
    remaining = available_seats - passengers[i]

    print("\nRoute:", routes[i])
    print("Passengers:", passengers[i])
    print("Buses Required:", buses)
    print("Extra Seats:", remaining)

    total_buses += buses

print("\nTotal Buses Required:", total_buses)
print("Unserved Passengers:", unserved)
