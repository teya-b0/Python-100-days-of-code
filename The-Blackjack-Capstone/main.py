import subprocess
from art import logo
from functions import deal_card, calculate_score, compare

print(logo)
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.\n: ").lower()

if start_game == "y":
    new_game = True

    while new_game:
        user_cards = []
        computer_cards = []
        subprocess.run("clear")
        print(logo)

        user_cards = deal_card(cards=user_cards, f_hand=True)
        computer_cards = deal_card(cards=computer_cards, f_hand=True)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        should_continue = input("Type 'y' to get another card, type 'n' to pass.\n: ").lower()
        if should_continue == "y":
            should_continue = True
            while should_continue:
                subprocess.run("clear")
                print(logo)
                user_cards = deal_card(cards=user_cards, f_hand=False)
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                result = compare(u_score=user_score, c_score=computer_score, should_cont=True)

                if result is None:
                    should_continue = input("Type 'y' to get another card, type 'n' to pass.\n: ").lower()
                    if should_continue == "n":
                        subprocess.run("clear")
                        print(logo)
                        while computer_score < 17:
                            computer_cards = deal_card(cards=computer_cards, f_hand=False)
                            computer_score = calculate_score(computer_cards)
                        result = compare(u_score=user_score, c_score=computer_score, should_cont=False)
                        print(f"Your final hand: {user_cards}, final score: {user_score}")
                        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                        print(result)
                        should_continue = False
                        n_game = input("Start a new game? Type 'y' or 'n'.\n: ").lower()

                        if n_game == "n":
                            new_game = False

                else:
                    subprocess.run("clear")
                    print(logo)
                    while computer_score < 17:
                        computer_cards = deal_card(cards=computer_cards, f_hand=False)
                        computer_score = calculate_score(computer_cards)
                    result = compare(u_score=user_score, c_score=computer_score, should_cont=False)
                    print(f"Your final hand: {user_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print(result)
                    should_continue = False

                    n_game = input("Start a new game? Type 'y' or 'n'.\n: ").lower()

                    if n_game == "n":
                        new_game = False
        else:
            subprocess.run("clear")
            print(logo)
            while computer_score < 17:
                computer_cards = deal_card(cards=computer_cards, f_hand=False)
                computer_score = calculate_score(computer_cards)
            result = compare(u_score=user_score, c_score=computer_score, should_cont=False)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(result)

            n_game = input("Start a new game? Type 'y' or 'n'.\n: ").lower()

            if n_game == "n":
                new_game = False

elif start_game == "n":
    print("Sorry to see you leave!")
    exit()
else:
    print("Invalid Input, please try again")
    exit()
