import sqlite3
import heapq

# Create database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients(
    PatientID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    PriorityLevel INTEGER,
    Status TEXT
)
""")

# Delete old records (optional)
cursor.execute("DELETE FROM Patients")

# ------------------ Dynamic Input ------------------

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nEnter Details of Patient", i + 1)

    pid = int(input("Patient ID: "))
    name = input("Patient Name: ")
    age = int(input("Age: "))
    priority = int(input("Priority Level (1 = Highest): "))

    cursor.execute(
        "INSERT INTO Patients VALUES (?,?,?,?,?)",
        (pid, name, age, priority, "Waiting")
    )

conn.commit()

# ------------------ Fetch Patients ------------------

cursor.execute("SELECT * FROM Patients WHERE Status='Waiting'")
patients = cursor.fetchall()

# ------------------ Priority Queue ------------------

pq = []

for p in patients:
    # Heap stores (priority, patient_id, full_record)
    heapq.heappush(pq, (p[3], p[0], p))

# ------------------ Attend Patients ------------------

print("\nPatients Attended in Priority Order\n")

while pq:
    priority, pid, patient = heapq.heappop(pq)

    print("Patient ID :", patient[0])
    print("Name       :", patient[1])
    print("Age        :", patient[2])
    print("Priority   :", patient[3])
    print("--------------------------")

    # Update status
    cursor.execute(
        "UPDATE Patients SET Status='Attended' WHERE PatientID=?",
        (pid,)
    )

conn.commit()

# ------------------ Remaining Patients ------------------

print("\nRemaining Patients\n")

cursor.execute("SELECT * FROM Patients WHERE Status='Waiting'")
remaining = cursor.fetchall()

if len(remaining) == 0:
    print("No patients are waiting.")
else:
    for p in remaining:
        print(p)

conn.close()