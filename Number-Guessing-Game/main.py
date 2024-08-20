from art import LOGO
from functions import game
import subprocess

print(LOGO)
print("Welcome to the Number Guessing Game!")
start = input("Would you like to play a game? Type 'Y' or 'N'\n:").lower()

if start == "y":
    restart = True

    while restart:
        subprocess.run("clear")
        print(LOGO)
        print("I'm thinking of a number between 1 and 100.")
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

        if difficulty_level == "easy" or difficulty_level == "hard":
            should_continue = game(df_level=difficulty_level)

            if should_continue == "y":
                subprocess.run("clear")

            elif should_continue == "n":
                restart = False
                subprocess.run("clear")
                print(LOGO)
                print("Sorry to see you go, come back soon!")
                exit()

            else:
                restart = False
                print("Invalid Input, Try again.")
                exit()

        else:
            print("Invalid Input, Try again.")
            exit()


elif start == "n":
    print("Sorry to see you go, come back soon!")
    exit()
else:
    print("Invalid Input, Try again.")
    exit()
