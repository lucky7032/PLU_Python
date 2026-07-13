patients = input("Enter patient names: ").split()
priority = list(map(int, input("Enter priorities: ").split()))

data = list(zip(priority, patients))

data.sort(reverse=True)

print("Emergency Queue:")

for p, name in data:
    print(name, "-", p)
