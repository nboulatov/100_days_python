from game_data import data
import random

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # generage a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a==account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You are right {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong {score}")