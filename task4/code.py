# Case Study 54: Branch Expense Analysis

branches = [
    [1000, 1500, 1200],
    [2000, 1800, 1600],
    [900, 1100, 1300]
]

names = ["Branch A", "Branch B", "Branch C"]
highest = 0
highest_branch = ""

for i in range(len(branches)):
    total = sum(branches[i])
    average = total / len(branches[i])

    print(names[i])
    print("Total Expenses:", total)
    print("Average Expense:", average)

    if total > highest:
        highest = total
        highest_branch = names[i]

print("\nHighest Expense:", highest_branch)
print("Amount:", highest)
