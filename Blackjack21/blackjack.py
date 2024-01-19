import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Welcome to Blackjack21! Would you like to play? Type 'y' or 'n'.\n")

if start == "y":
    game_over = False
else:
    game_over = True
    print("Boo you whore")

def deal_card(player, amount):
    for c in range(amount):
        card = random.choice(cards)
        player.append(card)

def check_total(hand):
    total = sum(hand)
    return total

def player_turn():
    draw = input("Do you want to draw another card? Type 'y' or 'n'.\n")
    if draw == "y":
        deal_card(player_hand, 1)
        if check_total(player_hand) < 21:
            print(f"Your cards: {player_hand}\nYour total: {check_total(player_hand)}")
            player_turn()
        elif check_total(player_hand) > 21:
            print(f"Your cards: {player_hand}\nYour total: {check_total(player_hand)} You busted!")
            return "bust"
    else:
        return "stand"

def dealer_turn():
    while check_total(comp_hand) < 16:
        deal_card(comp_hand, 1)
        if check_total(comp_hand) > 21:
            return "Dealer bust"
    return "Dealer stand"

def check_winner():
    if check_total(player_hand) > check_total(comp_hand):
        winner = "Player"
    else:
        winner = "Dealer"
    return winner


while not game_over:
    comp_hand = []
    player_hand = []

    #Deal first cards
    deal_card(comp_hand, 2)
    deal_card(player_hand, 2)

    if check_total(comp_hand) == 21:
        print("Dealer got blackjack, you lose.")
        game_over = True
    elif check_total(player_hand) == 21:
        print("You got blackjack, you win!")
        game_over = True
    else:
        player_total = check_total(player_hand)
        comp_total = check_total(comp_hand)
        print(f"Your cards are {player_hand} and your total is {player_total}")
        print(f"Dealer's first card is {comp_hand[0]} whole hand {comp_hand}")
        if player_turn() == "bust":
            game_over = True
        else:
            print("Player stand")
            print(dealer_turn())
            if dealer_turn() == "Dealer bust":
                print("Dealer busted, you win!")
                game_over = True
            else:
                print(f"Your total is {check_total(player_hand)} \nDealer total is {check_total(comp_hand)}\nThe winner is {check_winner()}") 
                game_over = True



    