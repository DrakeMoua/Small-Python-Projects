#Simple Numbers game with a bit of a twist

from random import randint as rint
from random import uniform
import time

dm = ["easy", "normal", "hard", "impossible"]
numbs = [10, 100, 1000, 1000]
check = True
count = 0

while check == True:
    try:
        difficulty = input("Please select a difficulty by typing a number: '0 - easy' '1 - normal' '2 - hard' '3 - impossible'")
        difficulty = int(difficulty)
        if difficulty < 0 or difficulty > 3:
            print("Please enter an integer between 0 and 3!")
        else:
            break
    except:
        print("Please enter an integer between 0 and 3!")

print("The difficulty you have selected is", dm[difficulty], "mode")
print("You will be guessing a number between 1 and", numbs[difficulty])

if difficulty == 3:
    print("The number will have two decimal places that you also need to find")
    gamenumb = round(uniform(1, 1000), 2)

else:
    gamenumb = rint(1, numbs[difficulty])

while check == True:
    print("Guesses:", count)
    guess = input("Please enter your guess here. Type 'quit' to leave")

    if guess == "quit":
        print("You lose with ", count, "Guesses. The number was", gamenumb)
        break
    try:
        guess = float(guess)

        if guess < gamenumb:
            print("The number is higher than", guess)
            count += 1
            continue

        elif guess > gamenumb:
            print("The number is lower than", guess)
            count += 1
            continue

        else:
            count += 1
            print("Congratulations you guessed the number", gamenumb, "in", count, "Guesses")
            time.sleep(5)
            break

    except:
        print("Invalid Input")
