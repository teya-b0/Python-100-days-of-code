import time
from art import logo
import subprocess

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar(cipher_direction, start_text, shift_amount):
    if cipher_direction == "decode":
        shift_amount *= -1
    message = ""
    for letter in start_text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % 26
            message += alphabet[new_position]
        else:
            message += letter
    print(f"The {cipher_direction}d text is {message}")


def rerun_caesar():
    subprocess.run("clear")
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        rerun_check()
    else:
        print("Invalid input, Please try again.")
        time.sleep(3)
        rerun_caesar()


def rerun_check():
    go_again = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if go_again == "yes":
        rerun_caesar()
    elif go_again == "no":
        print("Thanks for using the Caesar Cipher, Goodbye!")
    else:
        print("Invalid input, Please try again.")
        time.sleep(3)
        rerun_check()


rerun_caesar()
