# Case Study 58: Library Fine Calculation

books = [
    ("B101", 3),
    ("B102", 0),
    ("B103", 5),
    ("B104", 2)
]

fine_per_day = 5
total_fine = 0

for book_id, delay in books:
    fine = delay * fine_per_day
    total_fine += fine

    print("\nBook ID:", book_id)
    print("Days Overdue:", delay)
    print("Fine: Rs.", fine)

    if delay > 0:
        print("Status: Overdue")
    else:
        print("Status: Returned on time")

print("\nTotal Fine: Rs.", total_fine)
