# Case Study 52: Hackathon Team Ranking

teams = [
    ("Team A", [80, 90, 85]),
    ("Team B", [75, 88, 92]),
    ("Team C", [90, 95, 89])
]

for team, scores in teams:
    total = sum(scores)
    print(team, "Total Score:", total)

teams.sort(key=lambda x: sum(x[1]), reverse=True)

print("\nTeam Rankings:")
rank = 1

for team, scores in teams:
    print(rank, team, "Score:", sum(scores))
    rank += 1
