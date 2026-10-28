# Case Study 60: Quality Control

products = ["Product A", "Product B", "Product C"]
batches = [
    [100, 5],
    [200, 30],
    [150, 10]
]

limit = 10

for i in range(len(products)):
    produced = batches[i][0]
    defective = batches[i][1]

    percentage = (defective / produced) * 100

    print("\nProduct:", products[i])
    print("Units Produced:", produced)
    print("Defective Units:", defective)
    print("Defect Percentage:", round(percentage, 2), "%")

    if percentage > limit:
        print("Quality Check: Failed")
    else:
        print("Quality Check: Passed")
