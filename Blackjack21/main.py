import random
import sys, subprocess
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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
                return sum(hand)
    return total


def run_game(dealer_score, player_score):
    
    if player_score > 21 and dealer_score > 21:
        return "Both bust. Draw"
    elif player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Dealer got blackjack. Player loses!"
    elif player_score == 0:
        return "Player got blackjack. Player wins!"
    elif player_score > 21:  
        return f"Player bust! Score {player_score} - Player loses!"
    elif dealer_score > 21:
        return f"Dealer bust! Score {dealer_score} - Player wins!"
    elif player_score > dealer_score:
        return "Player wins!"
    else:
        return "Dealer wins!"
    



def play():
    comp_hand = []
    player_hand = []
    deal_card(comp_hand, 2)
    deal_card(player_hand, 2)
    game_over = False
    
    while not game_over:
        dealer_score = calculate_score(comp_hand)
        player_score = calculate_score(player_hand)
        print(f"Player hand: {player_hand} and total {player_score}\nDealer's first card is {comp_hand[0]}")

        if dealer_score == 0 or player_score == 0 or player_score > 21:
            game_over = True
        else:
            end_turn = False
            while not end_turn:
                deal_again = input("Does Player want another card? Type 'y' or 'n'.\n")
                if deal_again == "y":
                    deal_card(player_hand, 1)
                    player_score = calculate_score(player_hand)
                    print(f"Player hand: {player_hand} and total {player_score}")
                else:
                    print("Player stand")
                    end_turn = True

        while dealer_score != 0 and dealer_score < 17:
            deal_card(comp_hand, 1)
            dealer_score = calculate_score(comp_hand)
            

        print(f"Player total: {player_score}\nDealer total: {dealer_score}")
        print(run_game(dealer_score, player_score))
        game_over = True


start = input("Welcome to Blackjack21! Would you like to play? Type 'y' or 'n'.\n")

if start == "y":
    subprocess.run("clear", shell=True)
    play()
else:
    print("Boo you whore")