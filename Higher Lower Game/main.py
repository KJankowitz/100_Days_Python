import random
from game_data import data

#things to compare
A = data[0]
B = ""

#1 pick random dict from data list and assign to B
n = random.randint(1, len(data))
B = data[n]

#2 display all info exept followers?
print(f"Option A: {A["name"]}, a {A["description"]} from {A["country"]}")
print(f"Option B: {B["name"]}, a {B["description"]} from {B["country"]}")

#3 compare A and B and save answer?
ANSWER = ""
if A["follower_count"] > B["follower_count"]:
    ANSWER = "A"
else:
    ANSWER = "B"

#4 Ask user to guess who has more followers, A or B
player_score = 0
guess = input("Which one has more followers? Type 'A' or 'B'\n")
if guess.upper() == ANSWER:
    player_score += 1
    print(f"Correct! Your score is {player_score}")
else:
    print("game over")

#5 If user correct, display score and add 1

#6 If user incorrect, game over

#7 replace A with B and compare new random B. (repeat #1 - #6)

#8 Add play again loop