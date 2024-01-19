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
    if total == 21:
        if player == comp_hand:
            print("Dealer got Blackjack! You Lose")
        else:
            print("You got Blackjack! You win")
    elif total > 21:
        if 11 in player:
            ace = player.index(11)
            player[ace] = 1
            return sum(player)
        else:
            print(f"{player} busted, {total}")
    else:
        return total

def end_turn(player):
    hand_total = count_hand(player)
    if player == player_hand:
        print(f"Your cards are {player_hand} and your total is {hand_total}")

print(f"Dealer's first card is {comp_hand[0]}")
end_turn(player_hand)

deal_again = input("Do you want another card? Type 'y' or 'n'.\n")

if deal_again == "y":
    deal_card(player_hand, 1)
    count_hand(player_hand)
    end_turn(player_hand)
else:
    count_hand(comp_hand)
    if count_hand(comp_hand) < 16:
        deal_card(comp_hand, 1 )
        count_hand(comp_hand)