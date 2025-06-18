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
