import random

num = random.randomint(1, 100)
guesses = 0
level = input("Which diffculty do you want? Type 'hard' or 'easy'./n")

if level == "hard":
    guesses = 5
elif level == "easy":
    guesses = 10



def check_guess():
    if player_guess > num:
        guesses -= 1
        return "Too high"
    elif player_guess < num:
        guesses -= 1
        return "Too low"
    elif player_guess == num:
        return f"You won! The number was {num}"
    
while guesses > 0:
    player_guess = input("Guess the number")
    check_guess()
    print(f"You have {guesses} guesses left.")




