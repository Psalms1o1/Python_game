import random
import re

def play_rps():
    # Clear screen
    while True:
        print("\nRock, Paper, Scissors - Shoot!")
        user_choice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ").upper()

        # Validate user input
        if not re.match("^[RPS]$", user_choice):
            print("Invalid input! Please enter R, P, or S.")
            continue

        print("You chose:", user_choice)
        choices = ['R', 'P', 'S']
        opponent_choice = random.choice(choices)
        print("I chose:", opponent_choice)

        # Game result logic
        if user_choice == opponent_choice:
            print("It's a Tie!")
        elif (user_choice == 'R' and opponent_choice == 'S') or \
             (user_choice == 'P' and opponent_choice == 'R') or \
             (user_choice == 'S' and opponent_choice == 'P'):
            print("You Win!")
        else:
            print("I Win!")

# Run the game
play_rps()
