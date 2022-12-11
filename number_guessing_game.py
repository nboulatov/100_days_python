import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1,100)
print(chosen_number)
difficulty = input("Type 'easy' or 'hard' for difficulty: ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print("You win")
        attempts = 1
    elif guess < chosen_number:
        print("Too low")
    elif guess > chosen_number:
        print("Too high")
    attempts -=1
if attempts == 0 and guess != chosen_number:
    print("You've run out of guesses, you lose")
