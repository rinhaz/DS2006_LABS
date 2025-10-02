from dice import roll_d6, roll_d20

winning_score = 3
rounds = 0
gameover = False
players = []

number_of_players = int(input("How many players? : "))

for i in range(number_of_players):
    player = {
        "name": input(f"What is the name of player {i + 1}? "),
        "wins": 0,
        "rolls": []
    }
    players.append(player)

while not gameover:
    print(f"\nRound {rounds + 1}:")
    current_rolls = []

    for player in players:
        roll = roll_d6() + roll_d20()
        player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"Player {player['name']} rolled: {roll}")

    input("\nPress Enter to continue")

    max_roll = max(current_rolls)
    winners = []

    for player in players:
        if player["rolls"][-1] == max_roll:
            player["wins"] += 1
            winners.append(player["name"])

    print(f"Winners of this round: {', '.join(winners)}")

    for player in players:
        if player["wins"] >= winning_score:
            print(f"\n{player['name']} is the newest Battle of Dice Champion!")
            gameover = True

    if not gameover:
        print("This heated Battle of Dices is still going on! Who will win in the end?")
        rounds += 1


filename = input("\nEnter the file name to save results: ")
with open(filename, "w") as file:
    file.write("Player information:\n\n")
    for player in players:
        file.write(
            f"Name: {player['name']}\n"
            f"* Wins: {player['wins']}\n"
            f"Rolls: {player['rolls']}\n\n"
        )

    for r in range(rounds):
        rolls_str = ""
        for i, player in enumerate(players):
            rolls_str += f"{player['name']} rolled {player['rolls'][r]}"
            if i < len(players) - 1:
                rolls_str += ", "
        file.write(f"Round {r + 1}: {rolls_str}\n")

print("\nGame Over! Results saved successfully")
