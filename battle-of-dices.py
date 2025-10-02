import random

print(" Welcome to Battle of Dices! ")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("Press ENTER to roll the dice...")

print("Player 1 rolled: ", player1_roll)

player1_roll = random.randint(1, 6)

print("Player 2 rolled: ", player2_roll)

player2_roll = random.randint(1, 6)

input("Press ENTER to continue...")


if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)


print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")


if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")




