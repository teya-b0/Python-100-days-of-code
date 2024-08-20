import random


def game(df_level):

    if df_level == "easy":
        lives = 10
    else:
        lives = 5

    rand_num = random.randint(1, 100)

    end_game = False
    while not end_game:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\n").lower())

        if guess == rand_num:
            print(f"You got it! The answer was {rand_num}")
            end_game = True
        elif guess < rand_num:
            print("Too low.")
            lives -= 1
            if lives == 0:
                print("You've run out of guesses, you lose.")
                end_game = True
            else:
                print("Guess again.")
        elif guess > rand_num:
            print("Too high.")
            lives -= 1
            if lives == 0:
                print("You've run out of guesses, you lose.")
                end_game = True
            else:
                print("Guess again.")
        else:
            print("Invalid input, Try again.")

    should_cont = input("Would you like to play another game? Type 'Y' or 'N'\n:").lower()
    return should_cont
