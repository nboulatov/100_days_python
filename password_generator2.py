import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to the Password Generator")
number_of_letters=int(input("How many letters would you like\n"))
number_of_numbers=int(input("How many numbers would you like\n"))
number_of_symbols=int(input("How many symbols would you like\n"))
password = ''
for item in range(1,number_of_letters+1):
    password+= random.choice(letters)
for item in range(1,number_of_numbers+1):
    password+= random.choice(numbers)
for item in range(1,number_of_symbols+1):
    password+= random.choice(symbols)
password_length = len(password)
password2 = list(password)
new_password = ''
for item in range(1,password_length):
    new_password+=random.choice(password2)
print(new_password)
