import random
from game_data import data
import sys, subprocess
from art import logo, vs

play_game = True
A = data[0]
B = ""
player_score = 0

while play_game:
    subprocess.run("clear", shell=True)
    n = random.randint(1, len(data))
    B = data[n]
    print(logo)
    print(f"Your current score is {player_score}")
    print(f"Option A: {A["name"]}, a {A["description"]} from {A["country"]}")
    print(vs)
    print(f"Option B: {B["name"]}, a {B["description"]} from {B["country"]}")

    ANSWER = ""
    if A["follower_count"] > B["follower_count"]:
        ANSWER = "A"
    else:
        ANSWER = "B"

    guess = input("Which one has more followers? Type 'A' or 'B'\n")
    if guess.upper() == ANSWER:
        player_score += 1
        print(f"Correct! Your score is {player_score}")
    else:
        print("Nope! Game over")
        play_game = False

    A = B

#bugfix - when A and randint B is the same
#8 Add play again loop