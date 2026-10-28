# Case Study 51: Bus Passenger Occupancy

capacity = 50
passengers = 0

stops = 4

for i in range(1, stops + 1):
    boarding = int(input("Passengers boarding: "))
    alighting = int(input("Passengers alighting: "))

    passengers = passengers + boarding - alighting

    if passengers < 0:
        print("Invalid passenger count")
        passengers = 0
    elif passengers > capacity:
        print("Capacity exceeded!")

    print("Stop:", i)
    print("Passengers inside:", passengers)
