# Case Study 57: Canteen Management

items = ["Idli", "Dosa", "Meals"]
prices = [30, 50, 80]
stock = [20, 15, 10]

sales = 0

for i in range(3):
    print(i + 1, items[i], "- Rs.", prices[i],
          "- Stock:", stock[i])

    quantity = int(input("Enter quantity to order: "))

    if quantity <= 0:
        print("Invalid quantity")
    elif quantity <= stock[i]:
        bill = quantity * prices[i]
        stock[i] -= quantity
        sales += bill

        print("Bill: Rs.", bill)
        print("Order successful")
    else:
        print("Not enough stock")

print("\nTotal Sales: Rs.", sales)
print("Remaining Stock:", stock)
