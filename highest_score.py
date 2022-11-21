input_scores = input("Enter student scores ").split(",")
student_scores = []
for items in input_scores:
    items = int(items)
    student_scores.append(items)
score = 0
for item in student_scores:
    if item > score:
        score = item
print(f"The highest score in the class is: {score}")