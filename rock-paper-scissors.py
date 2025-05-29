import random
import time

# Prints out a delayed string
def print_slow(str):
    for char in str:
        print(char, end="")
        time.sleep(0.05)
    print("\n")

# This will be where the main function for our game is
def game():
    choices = ["rock", "paper", "scissors"]

    # Intro code
    print_slow("Welcome to Rock, Paper, Scissors!")
    print_slow("The rules are simple: \nRock crushes scissors, \nScissors cuts paper, \nPaper covers rock.")
    print_slow("Let's start the game!")

    while True:
        print_slow("Choose your weapon: rock, paper, or scissors")
        player_choice = input().lower()

        if player_choice not in choices:
            print_slow("Invalid choice. Please try again.")
            continue    

        print_slow("You chose: " + player_choice + ".. Now it's my turn to choose.")
        time.sleep(1)

        computer_choice = random.choice(choices)
        print_slow("I chose: " + computer_choice + ".")

        if player_choice == computer_choice:
            print_slow("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print_slow("You win!")
        else:
            print_slow("I win!")

        print_slow("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            print_slow("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    game()
