def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
n1 = int(input("What is the 1st #? "))
n2 = int(input("What is the 2nd #? "))

for item in operations:
    print(item)
operation_symbol = input("Pick an operation from above")

calculation_function = operations[operation_symbol]
answer = calculation_function(n1,n2)

print(f"{n1}{operation_symbol}{n2} = {answer}")