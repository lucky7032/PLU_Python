n = int(input("Enter number of students: "))

roll_numbers = []

for i in range(n):
    roll = int(input("Enter roll number: "))
    roll_numbers.append(roll)

search_roll = int(input("Enter roll number to search: "))

found = False

for i in range(len(roll_numbers)):
    if roll_numbers[i] == search_roll:
        print("Student Found at position:", i + 1)
        found = True
        break
    

if found == False:
    print("Student Not Found")