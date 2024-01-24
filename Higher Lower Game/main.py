import random
from game_data import data

#things to compare
A = data[0]
B = ""

#1 pick random dict from data list and assign to B
n = random.randint(0, len(data))
B = data[n]

#2 display all info exept followers?
print(f"Option A: {A["name"]}, a {A["description"]} from {A["country"]}")
print(f"Option B: {B["name"]}, a {B["description"]} from {B["country"]}")

#3 compare A and B and save answer?

#4 Ask user to guess who has more followers, A or B

#5 If user correct, display score and add 1

#6 If user incorrect, game over

#7 replace A with B and compare new random B. (repeat #1 - #6)

#8 Add play again loop


