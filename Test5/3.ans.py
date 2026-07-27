import sqlite3

# ------------------ Database ------------------

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions(
    TransactionID INTEGER PRIMARY KEY,
    AccountNumber TEXT,
    Amount REAL,
    Date TEXT,
    Type TEXT
)
""")

# Delete old records (optional)
cursor.execute("DELETE FROM Transactions")

# ------------------ Dynamic Input ------------------

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nEnter Transaction", i + 1)

    tid = int(input("Transaction ID: "))
    account = input("Account Number: ")
    amount = float(input("Amount: "))
    date = input("Date (DD-MM-YYYY): ")
    ttype = input("Type (Credit/Debit): ")

    cursor.execute(
        "INSERT INTO Transactions VALUES (?,?,?,?,?)",
        (tid, account, amount, date, ttype)
    )

conn.commit()

# ------------------ Fetch Data ------------------

cursor.execute("SELECT * FROM Transactions")
transactions = cursor.fetchall()

# ------------------ Quick Sort ------------------

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2][2]      # Amount

    left = []
    middle = []
    right = []

    for x in arr:
        if x[2] < pivot:
            left.append(x)
        elif x[2] == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

transactions = quick_sort(transactions)

# ------------------ Display Sorted ------------------

print("\nTransactions Sorted by Amount\n")

for t in transactions:
    print(t)

# ------------------ Binary Search ------------------

transactions_by_id = sorted(transactions, key=lambda x: x[0])

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid][0] == key:
            return arr[mid]
        elif arr[mid][0] < key:
            low = mid + 1
        else:
            high = mid - 1

    return None

search_id = int(input("\nEnter Transaction ID to Search: "))

result = binary_search(transactions_by_id, search_id)

if result:
    print("\nTransaction Found")
    print("Transaction ID :", result[0])
    print("Account Number :", result[1])
    print("Amount         :", result[2])
    print("Date           :", result[3])
    print("Type           :", result[4])
else:
    print("Transaction Not Found")

# ------------------ Total Credit & Debit ------------------

total_credit = 0
total_debit = 0

for t in transactions:
    if t[4].lower() == "credit":
        total_credit += t[2]
    elif t[4].lower() == "debit":
        total_debit += t[2]

print("\nTotal Credit =", total_credit)
print("Total Debit =", total_debit)

# ------------------ Top 5 Highest Transactions ------------------

transactions_desc = sorted(transactions, key=lambda x: x[2], reverse=True)

print("\nTop 5 Highest Value Transactions\n")

count = min(5, len(transactions_desc))

for i in range(count):
    print(transactions_desc[i])

conn.close()