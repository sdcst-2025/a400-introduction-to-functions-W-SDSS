#play the game
#number guessing game

import random

count = 1

while True:
    cp = random.choice(10)
    w = input("Guess a number 0 to 10: ")
    if w == cp:
        print("You win!")
        print(f"You have guessed {count} time.")
    else:
        print("You wrong. Try again.")
        count += 1