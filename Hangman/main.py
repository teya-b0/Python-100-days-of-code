import random
import subprocess
import time

from hangman_words import word_list
from hangman_art import stages, logo

word = random.choice(word_list)
word_len = len(word)
display = []
lives = 6
end_game = False

print(logo)

for _ in word:
    display += "_"

print(f'Pssst, the solution is {word}.')

while not end_game:

    if "_" in display and lives > 0:
        user_choice = input("Guess a letter: ").lower()

        if user_choice in display:
            print(f"You've already guessed {user_choice}.")
            time.sleep(5)
            subprocess.run("clear")

        else:
            for position in range(word_len):
                if user_choice == word[position]:
                    display[position] = user_choice

        if user_choice not in word:
            print(f"You guessed {user_choice}, That's not in the word, You lose a life.")
            lives -= 1
            time.sleep(5)
            subprocess.run("clear")


            if lives == 0:
                end_game = True
                print("You lose.")

        print(f"{''.join(display)}")

    else:
        end_game = True
        print("You Win.")
    print(stages[lives])
