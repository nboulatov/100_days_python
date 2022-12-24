from game_data import data
import random

# ask user to guess
def user_guesses(A,B):
    """Takes 2 values and asks user to guess A or B and returns # of followers"""
    if input("Which one has more followers? A or B? ").upper() == 'A':
        user_guess = A[0]["follower_count"]
        return user_guess
    else:
        user_guess = B[0]["follower_count"]
        return user_guess

# compare the 2 selections
def actual(A,B):
    """Takes 2 values and returns the greatest # of followers"""
    if A[0]["follower_count"] > B[0]["follower_count"]:
        bigger = A[0]["follower_count"]
        return bigger
    else:
        bigger = B[0]["follower_count"]
        return bigger

# check if user guessed correctly
def compare_user_guess_to_actual(user_choice,actual_value):
    if user_choice == actual_value:
        user_guessed = True
        return user_guessed
    else:
        user_guessed = False
        return user_guessed

# incrase user score by 1 if correct
def score(result):
    if result == True:
        return 1
    else:
        return 0

# draw 2 random selections from a list and store values in a list
user_score = 0
game_continues = True
A = []
A.append(random.choice(data))

while game_continues:
    B = []
    B.append(random.choice(data))

    print(A[0])
    print(B[0])

    user_choice = user_guesses(A,B)
    actual_value = actual(A,B)
    result = compare_user_guess_to_actual(user_choice,actual_value)
    user_score +=score(result)

    # stop the game if user failed to guess correctly
    if score(result) == 1:
        game_continues = True
    else:
        game_continues = False

    # make the next comparison with a new value and the value that was False
    if A[0]["follower_count"] < B[0]["follower_count"]:
        A = A
    else:
        A = B
    print(f"Your score is {user_score}")
