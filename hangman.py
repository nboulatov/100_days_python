import random

lives = 5
word_list = ["ardvark","baboon","camel"]
death_stages = ['Beginner','intermediate','advanced','expert','grandmaster']
chosen_word = random.choice(word_list)
word_length=len(chosen_word)
print(chosen_word)
empty_list = []
for i in range(word_length):
    empty_list+="_"
print(empty_list)
while lives!=0:
    guess = input("Guess a letter ").lower()
    if guess in empty_list:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        if chosen_word[position]==guess:
            empty_list[position]=guess
    if not guess in chosen_word:
        lives -=1
        print(f"you have {lives} lives left")
        print(death_stages[lives])
    print(empty_list)
if '_' in empty_list:
    print("you Loose")
else:
    print("you win")