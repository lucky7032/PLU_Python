marks = list(map(int, input("Enter marks: ").split()))

for i in range(len(marks)):
    for j in range(len(marks) - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Sorted marks:", marks)