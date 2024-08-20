import random
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
print("Welcome to the PyPassword Generator!")
pass_limit = int(input("How long would you like your password to be?\n"))

if 22 <= pass_limit <= 199:

    nr_upper_letters = int(input("How many upper-case letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    reserved = nr_upper_letters + nr_numbers + nr_symbols
    req_to_gen = pass_limit - reserved

    for n in range(1, req_to_gen + 1):
        password += random.choice(lower_letters)

    for n in range(1, nr_upper_letters + 1):
        password += random.choice(upper_letters)

    for n in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    for n in range(1, nr_numbers + 1):
        password += random.choice(numbers)

    final_password = ''.join(random.sample(password, len(password)))

    print(final_password)

else:
    print("Password must be between 22 ~ 199")
