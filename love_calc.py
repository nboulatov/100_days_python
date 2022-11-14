name1 = input("What is your name ")
name2 = input("What is his/her name ")
string = name1+name2
lower_string = string.lower()
t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")
true = t+r+u+e
l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")
love = l+o+v+e
love_score = str(true) + str(love)
love_score_total = int(love_score)
if love_score_total < 10 or love_score_total > 90:
    print(f"Your score is {love_score_total}, you go together like coke and mentos")
elif 40 > love_score_total < 50:
    print(f"Your score is {love_score_total}, you are alright together")
else:
    print(f"Love Score is {love_score_total}")