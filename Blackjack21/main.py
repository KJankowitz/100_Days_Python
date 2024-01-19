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

def calculate_score(hand):
    total = sum(hand)
    if total == 21:
        return 0
    elif total > 21:
        for card in hand:
            if card == 11:
                hand.remove(card)
                hand.append(1)
                calculate_score(hand)
    return total


def run_game():
    dealer_score = calculate_score(comp_hand)
    player_score = calculate_score(player_hand)

    if dealer_score == 0:
        print("Dealer got blackjack. Player loses!")
        game_over = True
    elif player_score == 0:
        print("Player got blackjack. Player wins!")
        game_over = True
    elif player_score > 21:
        print(f"Player bust! Score {player_score} - Player loses!")
        game_over = True
    print(f"Player hand: {player_hand} and total {player_score}")
    print(f"Dealer's first card is {comp_hand[0]}")

def compare():
    if calculate_score(comp_hand) > calculate_score(player_hand):
        winner = "Dealer wins!"
        return winner
    elif calculate_score(comp_hand) == calculate_score(player_hand):
        winner = "Draw"
        return winner
    else:
        winner = "Player wins!"
        return winner
    


while not game_over:
    comp_hand = []
    player_hand = []
    deal_card(comp_hand, 2)
    deal_card(player_hand, 2)
    run_game()
    dealer_score = calculate_score(comp_hand)
    player_score = calculate_score(player_hand)

    end_turn = False
    while not end_turn:
        deal_again = input("Does Player want another card? Type 'y' or 'n'.\n")
        if deal_again == "y":
            deal_card(player_hand, 1)
            calculate_score(player_hand)
            run_game()
        else:
            print("end turn")
            end_turn = True

    while dealer_score < 17:
        deal_card(comp_hand, 1)
        dealer_score = calculate_score(comp_hand)
        print(dealer_score)

    result = compare()
    print(f"{result}\nPlayer total: {player_score}\nDealer score: {dealer_score}")
    game_over = True
