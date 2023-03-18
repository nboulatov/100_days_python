sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
new_sentence = sentence.split()
new_dict = {}
for word in new_sentence:
    count = len(word)
    new_dict.update({word:count})


new_dict2 = {word:len(word) for word in sentence.split()}
print(new_dict2)
print(new_dict)