branch1 = list(map(int, input("Enter Branch 1 salaries: ").split()))
branch2 = list(map(int, input("Enter Branch 2 salaries: ").split()))

salary = branch1 + branch2

salary.sort()

print("Salaries in ascending order:", salary)