money = input("Give me some money: ")
print("here is your money", money)

first_money = input("Taka de: ")
second_money = input("A taka de naile gairalamu: ")

# taking 2, 3 or multiple input and integer input.
a, b = map(int, input("Dui ta number deo (space diye): ").split())  # a, b, c for 3
print("Prothom number:", a)
print("Ditiyo number:", b)

numbers = list(map(int, input("Onk gula number deo (space diye): ").split()))
print("Tumi diyecho:", numbers)

number = int(input("Amake ekta number deo: "))  # python takes input as string


print(
    type(first_money)
)  # by default the input from the user will be a string type. Try to notice.

print(first_money, second_money)

total = (
    first_money + second_money
)  # and it will give a concatenated version of the two numbers.

print("total money I got", total)

first_money_int = int(first_money)  # this is typecasting
second_money_int = int(second_money)

print(type(first_money_int))  # now it will be an integer

print("finally the total money: ", first_money_int + second_money_int)

number = 42
string_number = str(number)
print(string_number)
