import random
rock = '''
------rock-----
'''
paper = '''
------paper-----
'''
scissors = '''
------scissors-----
'''
game_images = [rock,paper,scissors]

user_choice = int(input("What do you choose? Rock 0, Paper 1, Scissors 2.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid you lose.")
else:
    print(f"You chose {user_choice}")
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw")