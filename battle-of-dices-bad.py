import random
Player1_wins= 0
Player2_wins= 0

player1_roll = random.randint(1,12)
player2_roll=random.randint(1,12)

print("Player 1 rolled", player1_roll)
print("Player 2 rolled", player2_roll)

roundWinner = ""

if player1_roll > player2_roll:
    roundWinner = "Player 1"
    Player1_wins +=1
elif player2_roll > player1_roll:
    roundWinner = "Player 2"
    Player2_wins +=1

      
else:
    roundWinner = "tie"
    
if roundWinner == "tie":
    print("looks like we got a tie")
else: 
    print(f"{roundWinner} won this round!!")
    
print("Result")
print("player1 :", Player1_wins)
print("player2 :", Player2_wins)
    
#i definitely think that using loop would have made this progress way easier and faster. 
    
