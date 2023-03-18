import pandas

data = pandas.read_csv("nato_phonetic_alphabet.cvs")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)

user_input = input("Enter a word ").upper()
# split = list(user_input)
# for letter in split:
#     print(phonetic_dict.get(letter))
output = [phonetic_dict[letter] for letter in user_input]
print(output)