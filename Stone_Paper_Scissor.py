/*************  ✨ Windsurf Command 🌟  *************/
import random
import os 
import re
def re():
    os.system('cls' if os.name == 'nt' else 'clear')
    while (1 < 2):
        print ("\n")
        print ("Rock, Paper, Scissors - Shoot")
        userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors:").upper()
        if not re.match("[RPS]", userChoice):
        userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors:")
        if not re.match("[ssRrPp]", userChoice):
            print ("Please choose a letter:")
            print ("[R]ock, [S]cissors or [P]aper.")
            continue
        
        print ("You chose: " + userChoice)
        choices = ['R', 'P', 'S']
        opponentChoice = random.choice(choices)
        print ("I chose: " + opponentChoice)
        if opponentChoice == userChoice:
        if opponentChoice == str.upper(userChoice):
            print ("Tie!")
        elif (opponentChoice == 'R' and userChoice == 'S') or (opponentChoice == 'S' and userChoice == 'P') or (opponentChoice == 'P' and userChoice == 'R'):
            print ("I Win ")
        #if opponentChoice = str("R") and str.upper(userChoice) = "P"
        elif opponentChoice == 'R' and userChoice.upper() == 'S':
            print ("scissors beats rock, I Win ")
            continue
        elif opponentChoice == 'S' and userChoice.upper() == 'P':
            print ("Scissors beats paper, I win")
            continue
        elif opponentChoice == 'P' and userChoice.upper() == 'R':
            print ("Paper beat rock, I win ")
            continue
        else:
            print ("You win")
            print ("you win")

/*******  0ef2413f-5789-40f8-a6ca-e51f73f4514c  *******/