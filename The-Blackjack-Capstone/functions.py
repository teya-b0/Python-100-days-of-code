import random


def deal_card(cards, f_hand):

    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if f_hand:
        for n in range(0, 2):
            random_card = random.choice(cards_list)
            cards.append(random_card)
        return cards
    else:
        random_card = random.choice(cards_list)
        cards.append(random_card)
        return cards


def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
    elif score > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            score -= 10
            return score
        else:
            return score
    else:
        return score


def compare(u_score, c_score, should_cont):

    if should_cont:

        if u_score == 0 and c_score == 0:
            return "Wow.. You both got a Blackjack, It's a draw 🙃"
        if u_score == 0:
            return "Win with a Blackjack 😎"
        if c_score == 0:
            return "Lose, opponent has Blackjack 😱"
        if u_score > 21:
            return "You went over 21, You lose 😤"
    else:

        if u_score == 0 and c_score == 0:
            return "Wow.. You both got a Blackjack, It's a draw 🙃"
        if u_score == 0:
            return "Win with a Blackjack 😎"
        if c_score == 0:
            return "Lose, opponent has Blackjack 😱"
        if u_score > 21 and c_score > 21:
            return "You both got a score over 21, It's a draw 🙃"
        if u_score > 21:
            return "You went over 21, You lose 😤"
        if c_score > 21:
            return "Opponent went over 21. You win 😁"
        if u_score == c_score:
            return "It's a draw 🙃"
        if u_score > c_score:
            return "You win 😁"
        if u_score < c_score:
            return "You lose 😤"
