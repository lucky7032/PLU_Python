import sqlite3
from collections import deque

# ---------------- Database ----------------

conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

# Restaurant Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurant(
    RestaurantID INTEGER PRIMARY KEY,
    RestaurantName TEXT
)
""")

# Delivery Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Delivery(
    DeliveryID INTEGER PRIMARY KEY,
    Area TEXT
)
""")

# Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    OrderID INTEGER PRIMARY KEY,
    RestaurantID INTEGER,
    DeliveryID INTEGER,
    Status TEXT
)
""")

# Delete old records (Optional)
cursor.execute("DELETE FROM Restaurant")
cursor.execute("DELETE FROM Delivery")
cursor.execute("DELETE FROM Orders")

# ---------------- Dynamic Input ----------------

r = int(input("Enter number of Restaurants: "))

for i in range(r):
    print("\nRestaurant", i + 1)
    rid = int(input("Restaurant ID: "))
    name = input("Restaurant Name: ")

    cursor.execute("INSERT INTO Restaurant VALUES(?,?)", (rid, name))

d = int(input("\nEnter number of Delivery Areas: "))

for i in range(d):
    print("\nDelivery Area", i + 1)
    did = int(input("Delivery ID: "))
    area = input("Area Name: ")

    cursor.execute("INSERT INTO Delivery VALUES(?,?)", (did, area))

o = int(input("\nEnter number of Orders: "))

for i in range(o):
    print("\nOrder", i + 1)

    oid = int(input("Order ID: "))
    rid = int(input("Restaurant ID: "))
    did = int(input("Delivery ID: "))

    cursor.execute(
        "INSERT INTO Orders VALUES(?,?,?,?)",
        (oid, rid, did, "Pending")
    )

conn.commit()

# ---------------- Fetch Pending Orders (JOIN) ----------------

cursor.execute("""
SELECT Orders.OrderID,
       Restaurant.RestaurantName,
       Delivery.Area,
       Orders.Status
FROM Orders
JOIN Restaurant
ON Orders.RestaurantID = Restaurant.RestaurantID
JOIN Delivery
ON Orders.DeliveryID = Delivery.DeliveryID
WHERE Orders.Status='Pending'
""")

orders = cursor.fetchall()

print("\nPending Orders\n")

for order in orders:
    print(order)

# ---------------- Graph ----------------

graph = {}

for order in orders:
    restaurant = order[1]
    area = order[2]

    if restaurant not in graph:
        graph[restaurant] = []

    graph[restaurant].append(area)

# ---------------- BFS ----------------

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("\nDelivery Order Sequence\n")

    while queue:
        node = queue.popleft()
        print(node)

        if node in graph:
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

# Start from first restaurant
if len(graph) > 0:
    start = list(graph.keys())[0]
    bfs(graph, start)

# ---------------- Update Orders ----------------

cursor.execute("UPDATE Orders SET Status='Completed' WHERE Status='Pending'")
conn.commit()

# ---------------- Display Updated Orders ----------------

print("\nUpdated Orders\n")

cursor.execute("SELECT * FROM Orders")

for row in cursor.fetchall():
    print(row)

conn.close()