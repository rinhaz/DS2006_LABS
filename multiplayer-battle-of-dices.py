from dice import roll_d6
winning_score = 3
Playernames=[]
player_wins=[]
player_rolls_history=[]
gameover = False
rounds= 0

player_numbers = int(input("How many player?"))

for i in range(player_numbers):
    name = input(f"What is the name of player {i+1}")
    Playernames.append(name)
    
for i in range(player_numbers):
    player_wins.append(0)
    
for i in range(player_numbers):
    player_rolls_history.append([])

while gameover is False:
    print(f"Round{ rounds +1}:")
    current_rolls= []
    
    for i in range(player_numbers):
        roll = roll_d6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {Playernames[i]} rolled:{roll}")
        
    input("\nPress Enter to continue")
    
    max_roll = max(current_rolls)
    winners = []
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(Playernames[j])
            player_wins[j] +=1
            print(f"Winners of this round are{winners}")
            
            for z in range(player_numbers):
                if player_wins [z] >= winning_score:
                    print(f" {Playernames[z]} is the newest battle of dice Champion!")
                    gameover = True
        if gameover is False:
            print("This heated Battle of Dices is still going on! Who will win in the end?")
        
        rounds +=1
                    
filename= input("Enter the file name to save results:")
with open(filename, "w") as file :
    for round_number in range(rounds):
        file.write(f"Round {round_number +1}:")
        rolls_str =""
        for i in range(player_numbers):
            rolls_str += (f"{Playernames [i]} rolled {player_rolls_history[i] [round_number]}")
            if i < player_numbers -1:
                rolls_str +=","
            print(f"Saving{rolls_str}")
            file.write(rolls_str +"\n")
                            
    