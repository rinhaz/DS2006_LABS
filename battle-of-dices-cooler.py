from dice import roll_d6, roll_d12
Player1_wins= 0
Player2_wins= 0
currentrounds = 0
gameover = False
while not gameover:
    input("Press enter to roll")
    
    player1_roll = roll_d6() + roll_d12()
    player2_roll = roll_d6() + roll_d12()
    
    print("player 1 rolled" ,player1_roll)
    print("Player 2 rolled", player2_roll)
    
    currentrounds += 1
    
    if player1_roll > player2_roll:
        roundWinner = "Player 1"
        Player1_wins += 1
    elif player1_roll < player2_roll:
        roundWinner = "Player 2"
        Player2_wins += 1   
    else:
        roundWinner = "tie"
        print("its a tie")

    if roundWinner == "tie":
        print("looks like we got a tie")
    else: 
        print(f"{roundWinner} won this round, it took {currentrounds} rounds")
    
    print("Result")
    print("player1 :", Player1_wins)
    print("player2 :", Player2_wins)

    if Player1_wins == 3:
        print("Player 1 is the Battle of Dices Champion!")
        gameover = True
    elif Player2_wins == 3:
        print("Player 2 is the Battle of Dices Champion!")
        gameover = True

    

    


    
    