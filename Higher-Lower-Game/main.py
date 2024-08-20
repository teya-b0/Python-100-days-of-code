from art import LOGO, VS
from game_data import data
import subprocess
import random
import time


def clear():
    subprocess.run("clear")


def game():
    restart = True

    while restart:
        should_cont = True
        score = 0
        b = random.choice(data)

        while should_cont:
            clear()
            print(LOGO)
            print(f"Current score: {score}.")

            a = b
            b = random.choice(data)
            while a == b:
                b = random.choice(data)

            print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}\n{VS}")
            print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

            user_answer = input("Who has more followers? Type 'A' or 'B'.\n:").lower()

            if user_answer == 'a' and a['follower_count'] > b['follower_count'] or \
                    user_answer == 'b' and b['follower_count'] > a['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
                time.sleep(3)

            else:
                clear()
                print(LOGO)
                should_cont = False
                print(f"Sorry, that's wrong. Final score: {score}")

                if input("Would you like to start a new game? Type 'y' or 'n'.\n:").lower() == "n":
                    restart = False


def run():
    print(LOGO)
    start = input("Welcome to the Higher Lower Game.\nWould you like to start? Type 'Y' or 'N'.\n:").lower()

    if start == "y":
        game()

    elif start == "n":
        print("Sorry to see you leave, Come back soon.")
        exit()
    else:
        print("Invalid input, Try again.")
        exit()


run()
