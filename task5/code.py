# Case Study 55: Transaction Audit

transactions = [
    (101, 500, "Deposit"),
    (102, 1000, "Withdrawal"),
    (103, -200, "Deposit"),
    (101, 700, "Deposit")
]

ids = []

for transaction in transactions:
    tid, amount, kind = transaction

    print("\nTransaction:", tid)

    if tid in ids:
        print("Duplicate transaction ID")
    else:
        ids.append(tid)

    if amount <= 0:
        print("Invalid amount")
    else:
        print("Amount:", amount)

    if kind not in ("Deposit", "Withdrawal"):
        print("Invalid transaction type")
