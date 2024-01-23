import random
play_again = True

while play_again:
    num = random.randint(1, 100)
    guesses = 0
    level = input("Which diffculty do you want? Type 'hard' or 'easy'.\n")

    if level == "hard":
        guesses = 5
    elif level == "easy":
        guesses = 10

    def check_lives():
        if player_guess > num:
            return - 1
        elif player_guess < num:
            return - 1
        else:
            return

    def check_guess():
        if player_guess > num:
            return "Too high"
        elif player_guess < num:
            return "Too low"
        elif player_guess == num:
            return f"You won! The number was {num}"
        
    while guesses > 0:
        player_guess = int(input("Guess the number\n"))
        print(check_guess())
        guesses = guesses + check_lives()
        print(f"You have {guesses} guess(es) left.")

    restart = input("Would you like to play again? Type 'y' or 'n'\n")
    if restart == "n":
        play_again == False



