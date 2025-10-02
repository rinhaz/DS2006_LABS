import random
Player1_wins= 0
Player2_wins= 0

#Round 1
player1_round1_roll1 = random.randint(1,6)
player2_round1_roll1=random.randint(1,6)

#Round 2
player1_round2_roll2 = random.randint(1,6)
player2_round2_roll2=random.randint(1,6)


#Round 3

player1_round3_roll3 = random.randint(1,6)
player2_round3_roll3=random.randint(1,6)

roundWinner = ""

print("Player 1 rolled :", player1_round1_roll1)
print("Player 2 rolled :", player2_round1_roll1)

if player1_round1_roll1 > player2_round1_roll1:
    roundWinner = "Player 1"
    Player1_wins +=1
elif player2_round1_roll1> player1_round1_roll1:
    roundWinner = "Player 2"
    Player2_wins +=1
else: roundWinner = "tie" 

if roundWinner == "tie":
    print("looks like its a tie")
else: print(f"{roundWinner} won the third round!!")
print("_________________________________")
print("Player 1 rolled :", player1_round2_roll2)
print("Player 2 rolled :", player2_round2_roll2)

    #round 2
if player1_round2_roll2 > player2_round2_roll2:
    roundWinner = "Player 1"
    Player1_wins +=1
elif player2_round2_roll2> player1_round2_roll2:
    roundWinner = "Player 2"
    Player2_wins +=1
else: roundWinner = "tie" 

if roundWinner == "tie":
    print("looks like its a tie")
else: print(f"{roundWinner} won the third round!!")
print("_________________________________")
print("Player 1 rolled :", player1_round3_roll3)
print("Player 2 rolled :", player2_round3_roll3)
 # round 3
if player1_round3_roll3> player2_round3_roll3:
    roundWinner = "Player 1"
    Player1_wins +=1
elif player2_round3_roll3> player1_round3_roll3:
    roundWinner = "Player 2"
    Player2_wins +=1 
else: roundWinner = "tie" 

if roundWinner == "tie":
    print("looks like its a tie")
else: print(f"{roundWinner} won the third round!!")

print("_________________________________")


print("Result:")
print("-----------------------------------------")
print("| Round    | 1 | 2 | 3 |")
print("-----------------------------------------")
print(f"| Player 1 | {player1_round1_roll1} | {player1_round2_roll2} | {player1_round3_roll3} |")
print("-----------------------------------------")
print(f"| Player 2 | {player2_round1_roll1} | {player2_round2_roll2} | {player2_round3_roll3} |")
print("-----------------------------------------")

    

    
