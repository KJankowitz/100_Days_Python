import random
from words import word_list
from art import logo
from art import stages

chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
game_over = False
lives = 6

print(logo)

for _ in range(word_length):
    display.append("_")
print(display)

index = 0

while not game_over:
    guess = input("Guess a letter\n").lower()
    if guess in display:
        print(f"{guess} has already been guessed")
    for n in range(word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = chosen_word[n]
    if guess not in chosen_word:
        print(f"{guess} is not in the word - lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You Lose!\nYour word was {chosen_word}")

    print(f"{''.join(display)}")

    if "".join(display) == chosen_word:
        game_over = True
        print("You win!")

    print(stages[lives])
