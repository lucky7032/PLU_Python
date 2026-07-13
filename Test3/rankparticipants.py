timings = list(map(float, input("Enter timings: ").split()))

for i in range(len(timings)):
    for j in range(len(timings) - 1):
        if timings[j] > timings[j + 1]:
            timings[j], timings[j + 1] = timings[j + 1], timings[j]

print("Fastest to slowest:", timings)