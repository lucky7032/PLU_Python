scores = list(map(int, input("Enter player scores: ").split()))

scores.sort(reverse=True)

print("Leaderboard:", scores)