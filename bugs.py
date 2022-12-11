# def f():
#     for i in range(20):
#         #print("ya")
#         if i == 20:
#             print("ya")
# f()

# import random
# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = random.randint(1,5)
# print(dice_imgs[dice_num])

# year = int(input("What is your birth year"))
# if year > 1980 and year <1994:
#     print("Millenial")
# elif year >=1994:
#     print("Gen z")

# age = int(input("How old are you?"))
# if age >18:
#     print(f"You can drive at age {age}")

# pages = 0
# word_per_page = 0
# pages = int(input("number of pages: "))
# word_per_page = int(input("Number of words per page:"))
# total_words = pages*word_per_page
# print(total_words)

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item*2
    b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])