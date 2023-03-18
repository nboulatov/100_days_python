def add(*arguments):
    sum = 0
    for number in arguments:
        sum+=number
    return sum
print(add(1,2,3,4,5,6,10))
def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add=5,multiply=4)