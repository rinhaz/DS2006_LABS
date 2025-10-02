from dice import roll_d6
    
Player1_wins= 0
Player2_wins= 0
gameover = False
while not gameover:
    input(" Press enter to roll")
    #round 1
    player1_round1_roll = roll_d6() 
    player2_round1_roll = roll_d6()
    
    #round 2
    
    player1_round2_roll = roll_d6() 
    player2_round2_roll = roll_d6()
    
    #round 3 
    
    player1_round3_roll = roll_d6() 
    player2_round3_roll = roll_d6()
    
    #round one
    print("Round 1:")
    print("Player 1 rolled",    player1_round1_roll)
    print("Player 2 rolled",    player2_round1_roll)
    
    if    player1_round1_roll >    player2_round1_roll:
        roundWinner = "Player 1"
        Player1_wins += 1
    elif    player1_round1_roll < player2_round1_roll:
        roundWinner = "Player 2"
        Player2_wins += 1   
    else:
        roundWinner = "tie"

    if roundWinner == "tie":
        print("looks like we got tie")
    else: print(f"{roundWinner} won the first round!!")
    
    
   #round two
    print("_________________________________________")
    print("Round 2: ")
    print("Player 1 rolled",    player1_round2_roll)
    print("Player 2 rolled",    player2_round2_roll)
   
    if    player1_round2_roll >    player2_round2_roll:
        roundWinner = "Player 1"
        Player1_wins += 1
    elif    player1_round2_roll < player2_round2_roll:
        roundWinner = "Player 2"
        Player2_wins += 1   
    else:
        roundWinner = "tie"

    if roundWinner == "tie":
        print("looks like we got tie")
    else: print(f"{roundWinner} won the second round!!")
    

    #round three
    print("_________________________________________")
    print("Round 3:")
    print("Player 1 rolled",    player1_round3_roll)
    print("Player 2 rolled",    player2_round3_roll)
    
    if  player1_round3_roll >    player2_round3_roll:
        roundWinner = "Player 1"
        Player1_wins += 1
    elif  player1_round3_roll < player2_round3_roll:
        roundWinner = "Player 2"
        Player2_wins += 1   
    else:
        roundWinner = "tie"

    if roundWinner == "tie":
        print("looks like we got tie")
    else: print(f"{roundWinner} won the third round!!")
    
    print("_____________________________")
    print("Result")
    print("Round :| 1 | 2 | 3 |")
    print(f"player1 : {player1_round1_roll} | {player1_round2_roll} | {player1_round3_roll}")
    print(f"player2 : {player2_round1_roll} | {player2_round2_roll} | {player2_round3_roll}")

    if Player1_wins == 1:
        print("Player 1 is the Battle of Dices Champion!")
        gameover = True
    
    elif Player2_wins == 1:
        print("Player 2 is the Battle of Dices Champion!")
        gameover = True

        

filename = input("Enter the name of the file to save the summary:")

with open(filename, "w") as file:
    file.write("Round :| 1 | 2 | 3 |\n")
    file.write(f"player1 : {player1_round1_roll} | {player1_round2_roll} | {player1_round3_roll}\n")
    file.write(f"player2 : {player2_round1_roll} | {player2_round2_roll} | {player2_round3_roll}\n")

print(f"Summary saved to {filename}")
