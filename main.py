import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_cards(no_cards=1):
    return random.sample(cards, no_cards)


def get_score(input_cards):
    score = sum(input_cards)

    if score > 21 and 11 in input_cards:
        while 11 in input_cards:
            input_cards.remove(11)
            input_cards.append(1)
        return sum(input_cards)
    return score


def get_computer_cards(comp_cards, opponent_score):
    comp_cards += get_cards()
    temp_score = get_score(comp_cards)
    while temp_score < 17 or (temp_score < opponent_score <= 21):
        comp_cards += get_cards()
        temp_score = get_score(comp_cards)
    return comp_cards


def print_temp_result(player_cards_arg, computer_cards_arg, player_score_arg):
    print(f"Your cards: {player_cards_arg}, current score: {player_score_arg}")
    print(f"Computer's first card: {computer_cards_arg[0]}")


def print_final_result(player_cards_arg, computer_cards_arg, player_score_arg, computer_score_arg):
    print(f"Your final hand: {player_cards_arg}, final score: {player_score_arg}")
    print(f"Computer's final hand: {computer_cards_arg}, final score: {computer_score_arg}")


def check_results(player_final_score, computer_final_score):
    if player_final_score == 21 and computer_final_score != 21:
        print("You win 😃")
    elif 21 > player_final_score > computer_final_score:
        print("You win 😃")
    elif player_final_score < 21 < computer_final_score:
        print("Opponent went over. You win 😁")
    elif computer_final_score > player_final_score:
        print("You lose 😭")
    else:
        print("Draw 🙃")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower() == "y":
    print(art.logo)
    player_cards = get_cards(2)
    computer_cards = get_cards(2)
    game_on = True
    while game_on:
        player_score = get_score(player_cards)
        print_temp_result(player_cards, computer_cards, player_score)

        if player_score > 21:
            computer_cards = get_computer_cards(computer_cards, player_score)
            computer_score = get_score(computer_cards)
            print_final_result(player_cards, computer_cards, player_score, computer_score)
            print("You went over. You lose 😭")
            game_on = False
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass:").lower() == "y"
            if new_card:
                player_cards += get_cards()
            else:
                computer_cards = get_computer_cards(computer_cards, player_score)
                computer_final_score = get_score(computer_cards)
                player_final_score = get_score(player_cards)
                print_final_result(player_cards, computer_cards, player_final_score, computer_final_score)
                check_results(player_final_score, computer_final_score)
                game_on = False
