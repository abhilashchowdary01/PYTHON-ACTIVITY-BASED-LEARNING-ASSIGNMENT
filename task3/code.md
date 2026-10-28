### Case Study 53: Food Waste Monitoring

### 1\. Problem Statement

Write a Python program to monitor food waste over four days. The program stores the quantities of food prepared and served each day. It calculates the amount of food wasted and its percentage. If the waste percentage exceeds 20%, display “Waste is above the limit”; otherwise, display “Waste is within the limit”.

### 2\. Algorithm

* Start.

* Create lists for food prepared and food served.

* Traverse each day's data using a `for` loop.

* Calculate waste by subtracting food served from food prepared.

* Calculate the waste percentage.

* Display the day, prepared quantity, served quantity, waste, and waste percentage.

* If the percentage exceeds 20%, print “Waste is above the limit”.

* Otherwise, print “Waste is within the limit”.

* Repeat for all four days.

* Stop.

### 3\. Flowchart (Mermaid Code)

```mermaid

flowchart TD
    A([Start]) --> B[Create prepared and served lists]
    B --> C[Set i = 0]
    C --> D{i < length of prepared?}
    D -- Yes --> E[Calculate waste = prepared[i] - served[i]]
    E --> F[Calculate percentage = waste / prepared[i] * 100]
    F --> G[Display daily details and percentage]
    G --> H{Percentage > 20?}
    H -- Yes --> I[Print Waste is above the limit]
    H -- No --> J[Print Waste is within the limit]
    I --> K[i = i + 1]
    J --> K
    K --> D
    D -- No --> L([Stop])
```

### 4\. Python Source Code

```python

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
```

### 5\. Sample Input

The program uses predefined lists, so no user input is required.

```text
Prepared = [100, 120, 150, 100]
Served   = [90, 100, 120, 80]
```

### 6\. Sample Output

```text
Day 1
Prepared: 100
Served: 90
Wasted: 10
Waste Percentage: 10.0 %
Waste is within the limit

Day 2
Prepared: 120
Served: 100
Wasted: 20
Waste Percentage: 16.67 %
Waste is within the limit

Day 3
Prepared: 150
Served: 120
Wasted: 30
Waste Percentage: 20.0 %
Waste is within the limit

Day 4
Prepared: 100
Served: 80
Wasted: 20
Waste Percentage: 20.0 %
Waste is within the limit
```

### 7\. Explanation

* `prepared` stores the quantity of food prepared each day.

* `served` stores the quantity of food served each day.

* `range(len(prepared))` accesses each day's data using its index.

* `waste = prepared[i] - served[i]` calculates the wasted food.

* `percentage` calculates the percentage of food wasted.

* `round(percentage, 2)` rounds the percentage to two decimal places.

* The `if-else` statement checks whether the waste percentage exceeds 20%.

