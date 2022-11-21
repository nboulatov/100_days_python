import random

your_choice = int(input("What do you choose? Rock 0, Paper 1, Scissors 2.\n"))
computer_choice = random.randint(0,2)
print(your_choice)
print(computer_choice)
if your_choice == 0 and computer_choice == 0:
    print("It's a draw")
elif your_choice == 0 and computer_choice == 1:
    print("You lose")
elif your_choice == 0 and computer_choice == 2:
    print("You win")
elif your_choice == 1 and computer_choice == 0:
    print("You win")
elif your_choice == 1 and computer_choice == 1:
    print("It's a draw")
elif your_choice == 1 and computer_choice == 2:
    print("You lose")
elif your_choice == 2 and computer_choice == 0:
    print("You lose")
elif your_choice == 2 and computer_choice == 1:
    print("You win")
elif your_choice == 2 and computer_choice == 2:
    print("It's a draw")