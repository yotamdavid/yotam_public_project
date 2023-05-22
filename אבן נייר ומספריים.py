# אבן נייר ומספריים
import random

print("Welcome to Rock-Paper-Numbers game!")
print("The rules are simple: Each player chooses rock, paper, or scissors. ")
print("Rock beats numbers, scissors beat paper, and paper beats rock. Let's begin!\n")

options = ["r", "p", "s"]
player1_score = 0
player2_score = 0

while True:
    # Get input from player 1
    while True:
        player1_choice = input("Player 1, choose rock (r), paper (p), or scissors (s): ")
        if player1_choice in options:
            break
        else:
            print("Invalid input, try again.\n")

    # Get input from player 2
    while True:
        player2_choice = input("Player 2, choose rock (r), paper (p), or scissors (s): ")
        if player2_choice in options:
            break
        else:
            print("Invalid input, try again.\n")

    # Determine the winner
    if player1_choice == player2_choice:
        print("Tie!")
    elif player1_choice == "r" and player2_choice == "s":
        print("Player 1 wins!")
        player1_score += 1
    elif player1_choice == "p" and player2_choice == "r":
        print("Player 1 wins!")
        player1_score += 1
    elif player1_choice == "s" and player2_choice == "p":
        print("Player 1 wins!")
        player1_score += 1
    else:
        print("Player 2 wins!")
        player2_score += 1

    # Show the current score
    print("Player 1: ", player1_score)
    print("Player 2: ", player2_score)
    print("\n")

    # Check if either player has won
    if player1_score == 3:
        print("Player 1 wins the game!")
        break
    elif player2_score == 3:
        print("Player 2 wins the game!")
        break