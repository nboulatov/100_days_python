new_list = [n+1 for n in [1,2,3]]
print(new_list)

new_list = [letter for letter in "Nikita"]
print(new_list)

new_list = [number*2 for number in range(1,5)]
print(new_list)

names = ["Nikita","Dred","Ncool","Vektra"]
short_names = [name for name in names if len(name)<5]
print(short_names)

names = ["Nikita","Dred","Ncool","Vektra"]
cap_names = [name.upper() for name in names if len(name)>5]
print(cap_names)