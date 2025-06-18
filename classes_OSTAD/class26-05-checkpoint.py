x, y, z = 2, 4, "c"
print(y, x)

x, y = 4, "tanvee"

fruits = ["apple", "banana", "orange"]
# list

import random

print(random.randrange(1, 10))

a, b = 4, 5

if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")


if not a > b:
    print("success")
else:
    print("failed")


a, b = map(int, input("space diye duita number deo: ").split())
x = input("+, -, *, / jekono ekta operator dao: ")

match x:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b if b != 0 else "OSHIM")
    case _:
        print("hobena")


# taking multiple inputs
