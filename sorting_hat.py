while True:
    command = input()
    team = ""

    if command == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break

    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(command) < 5:
        team = "Gryffindor"

    elif len(command) == 5:
        team = "Slytherin"

    elif len(command) == 6:
        team = "Ravenclaw"

    else:
        team = "Hufflepuff"

    print(f"{command} goes to {team}.")

