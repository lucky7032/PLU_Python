import sqlite3
import heapq

# ---------------- Database ----------------

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    RollNo INTEGER PRIMARY KEY,
    Name TEXT,
    CGPA REAL,
    Skills TEXT,
    PlacementStatus TEXT
)
""")

# Delete old records (Optional)
cursor.execute("DELETE FROM Students")

# ---------------- Dynamic Input ----------------

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter Details of Student", i + 1)

    roll = int(input("Roll Number: "))
    name = input("Name: ")
    cgpa = float(input("CGPA: "))
    skills = input("Skills: ")
    status = input("Placement Status (Placed/Not Placed): ")

    cursor.execute(
        "INSERT INTO Students VALUES(?,?,?,?,?)",
        (roll, name, cgpa, skills, status)
    )

conn.commit()

# ---------------- Fetch Data ----------------

cursor.execute("SELECT * FROM Students")
students = cursor.fetchall()

# ---------------- Heap Sort ----------------

heap = []

for student in students:
    # Heap based on CGPA
    heapq.heappush(heap, (student[2], student))

sorted_students = []

while heap:
    sorted_students.append(heapq.heappop(heap)[1])

print("\nStudents Sorted by CGPA\n")

for s in sorted_students:
    print(s)

# ---------------- Binary Search ----------------

students_by_roll = sorted(sorted_students, key=lambda x: x[0])

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

roll_search = int(input("\nEnter Roll Number to Search: "))

result = binary_search(students_by_roll, roll_search)

if result:
    print("\nStudent Found")
    print("Roll Number :", result[0])
    print("Name        :", result[1])
    print("CGPA        :", result[2])
    print("Skills      :", result[3])
    print("Status      :", result[4])
else:
    print("Student Not Found")

# ---------------- Eligible Students ----------------

print("\nStudents Eligible for Placement (CGPA > 7.5)\n")

eligible = False

for s in students_by_roll:
    if s[2] > 7.5:
        print(s)
        eligible = True

if not eligible:
    print("No Eligible Students")

# ---------------- Update Placement Status ----------------

roll_update = int(input("\nEnter Roll Number to Update Placement Status: "))
new_status = input("Enter New Status (Placed/Not Placed): ")

cursor.execute(
    "UPDATE Students SET PlacementStatus=? WHERE RollNo=?",
    (new_status, roll_update)
)

conn.commit()

# ---------------- Display Updated Records ----------------

print("\nUpdated Student Records\n")

cursor.execute("SELECT * FROM Students")

for student in cursor.fetchall():
    print(student)

conn.close()