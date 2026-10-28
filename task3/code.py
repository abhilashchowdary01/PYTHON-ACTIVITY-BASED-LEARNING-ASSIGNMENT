# Case Study 53: Food Waste Monitoring

prepared = [100, 120, 150, 100]
served = [90, 100, 120, 80]

for i in range(len(prepared)):
    waste = prepared[i] - served[i]
    percentage = (waste / prepared[i]) * 100

    print("\nDay", i + 1)
    print("Prepared:", prepared[i])
    print("Served:", served[i])
    print("Wasted:", waste)
    print("Waste Percentage:", round(percentage, 2), "%")

    if percentage > 20:
        print("Waste is above the limit")
    else:
        print("Waste is within the limit")


