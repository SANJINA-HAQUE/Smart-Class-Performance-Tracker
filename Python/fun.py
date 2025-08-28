import random

print("Welcome to the Guessing Game!")
number = random.randint(1, 10)  # The number to guess
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")

print(f"🎉 Congratulations! You guessed it right: {number}")
