from art import logo
import subprocess

first_bid = True
record = {}


def collect_bids(fst_bid):
    if fst_bid:
        print(f"{logo}\nWelcome to the secret auction program.")

    else:

        subprocess.run("clear")
        print(logo)

    name = input("What's your name?\n:")
    bid = int(input("What's your bid?\n: $"))
    record[name] = bid
    other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'.\n:").lower()

    if other_bidders == "yes":
        fst_bid = False
        collect_bids(fst_bid=fst_bid)
    else:
        winner = ""
        highest_bid = 0
        for name in record:
            if record[name] > highest_bid:
                winner = name
                highest_bid = record[name]

        subprocess.run("clear")
        print(logo)
        print(f"The winner is {winner} with a bid of ${highest_bid}")


collect_bids(fst_bid=first_bid)
