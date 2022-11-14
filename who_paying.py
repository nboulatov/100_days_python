import random


names = input("Type names of people separated by a comma ")
list = names.split(",")
print(len(list)-1)
payer = random.randint(0,len(list)-1)
print(f"{list[payer]} is paying for the bill.")