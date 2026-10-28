# Case Study 56: Student Group Formation

scores = [80, 70, 90, 60, 85, 75]
group1 = []
group2 = []

for i in range(len(scores)):
    if i % 2 == 0:
        group1.append(scores[i])
    else:
        group2.append(scores[i])

print("Group 1:", group1)
print("Group 1 Total:", sum(group1))

print("Group 2:", group2)
print("Group 2 Total:", sum(group2))

difference = abs(sum(group1) - sum(group2))
print("Difference between totals:", difference)
