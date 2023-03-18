PLACEHOLDER = "name"

with open("names.txt") as names:
    names = names.readlines()

with open("invitation.txt") as invitation:
    contents = invitation.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)