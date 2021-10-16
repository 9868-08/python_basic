players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_set=[]
for i in players:
    players_unated = i + players[i]
    players_set.append(players_unated)
print(players_set)