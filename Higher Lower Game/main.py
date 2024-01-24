import random
from game_data import data

play_game = True
#things to compare
A = data[0]
B = ""
player_score = 0

while play_game:
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
    guess = input("Which one has more followers? Type 'A' or 'B'\n")
    if guess.upper() == ANSWER:
        player_score += 1
        print(f"Correct! Your score is {player_score}")
    else:
        print("Nope! Game over")
        play_game = False

    #5 If user correct, display score and add 1
    #6 If user incorrect, game over

    #7 replace A with B and compare new random B. (repeat #1 - #6)

    A = B

#8 Add play again loop