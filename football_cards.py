team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

commands = input().split()
is_broken = False

for command in commands:
    team, player = command.split("-")
    if team == "A":
        if int(player) in team_A:
            team_A.remove(int(player))
    elif team == "B":
        if int(player) in team_B:
            team_B.remove(int(player))

    if len(team_A) < 7 or len(team_B) < 7:
        is_broken = True
        break


print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if is_broken:
    print('Game was terminated')