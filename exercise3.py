import random

number = random.randint(1, 100)
guess = 0

print("I chose a number between 1 and 100.\nGuess!")

while guess != number:
    guess = int(input("Please enter your guess: "))
    if guess < number:
        print("Please increase your guess!")
    elif guess > number:
        print("Please decrease your guess!")
    else:
        print("Congratulations! ")
        break

