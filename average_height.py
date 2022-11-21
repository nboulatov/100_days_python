student_heights = input("Input students heights").split()
list = []
for item in student_heights:
    item = int(item)
    list.append(item)

number_of_students = 0
for item in list:
    number_of_students +=1
combined_height = 0
for items in list:
    combined_height += items
average_height = combined_height/number_of_students
print(average_height)
print(round(average_height))
