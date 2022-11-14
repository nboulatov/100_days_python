year = int(input("Enter year "))
divide_4 = year%4
divide_100 = year%100
divide_400 = year%400
if divide_4 > 0:
    print("Not leap")
elif divide_4 == 0 and divide_100 > 0:
    print("Leap year")
elif divide_4 == 0 and divide_100 == 0 and divide_400 > 0:
    print("Not leap")
else:
    print("Leap year")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap")
    else:
        print("Leap year")
else:
    print("Not leap")