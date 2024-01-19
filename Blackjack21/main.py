import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Welcome to Blackjack21! Would you like to play? Type 'y' or 'n'.\n")

if start == "y":
    game_over = False
else:
    game_over = True
    print("Boo you whore")


comp_hand = []
player_hand = []

def deal_card(player, amount):
    for c in range(amount):
        card = random.choice(cards)
        player.append(card)

deal_card(comp_hand, 2)

deal_card(player_hand, 2)

def count_hand(player):
    total = sum(player)
    return total



hand_total = count_hand(player_hand)

print(f"Your cards are {player_hand} and your total is {hand_total}")

def check_blackjack(player):
    total = sum(player)
    if total == 21:
        if player == "comp_hand":
            print("Dealer got Blackjack! You Lose")
        else:
            print("You got Blackjack! You win")
#    elif total > 21:
#        if 11 in player:
