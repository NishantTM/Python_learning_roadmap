# 30. Create number guessing game in Python.

import random

print("Hi welcome to the number guessing game . You have 7 chances to win the game")
low = int(input("Enter the lower bound: "))
high = int(input("Enter the higher bound: "))

print("You have 7 chances to win game {low} {high}")

num = random.randint(low, high)

ch = 7
gc = 0

while True:
    gc < ch
    gc += 1
    guess = int(input("Enter your guess :"))

    if guess == num:
        print(f"The correct number is {num}. You guessed it in the correct {gc}")

    elif gc <= ch and guess != num:
        print(f" You guess the wrong number next time better lock :")

    elif guess > num:
        print("You guess to high")

    elif guess < num:
        print("You guess to low")
