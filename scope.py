enemies = 1

def increase_enemines():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemines()
print(f"enemies outside function: {enemies}")

x=3
def f():
   return x+3
print(f())
