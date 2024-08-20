import random
import art

art_list = [art.rock, art.paper, art.scissors]
print("Welcome to the Rock, Paper, Scissors Game!")

user_choice_str = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\nWhat do you choose?\n")
accepted_inputs = ["0", "1", "2"]

if user_choice_str in accepted_inputs:

    user_choice = int(user_choice_str)
    computer_choice = random.randint(0, 2)

    if user_choice == 0 and computer_choice == 2:
        print(f"{art_list[user_choice]}\nComputer Chose:\n{art_list[computer_choice]}\n You Win!")

    elif user_choice == 2 and computer_choice == 1:
        print(f"{art_list[user_choice]}\nComputer Chose:\n{art_list[computer_choice]}\n You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print(f"{art_list[user_choice]}\nComputer Chose:\n{art_list[computer_choice]}\n You Win!")

    elif user_choice == computer_choice:
        print(f"{art_list[user_choice]}\nComputer Chose:\n{art_list[computer_choice]}\n It's a draw!")

    else:
        print(f"{art_list[user_choice]}\nComputer Chose:\n{art_list[computer_choice]}\n You lose!")

else:
    print("Invalid Input, Please try again!")
