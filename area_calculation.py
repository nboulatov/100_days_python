import math


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
def paint_calc(height,width,cover):
    number_of_cans = (height*width)/cover
    cans = math.ceil(number_of_cans)
    print(f"You'll need {cans} cans of paint.")
paint_calc(height=test_h,width=test_w,cover=coverage)