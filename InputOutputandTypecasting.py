money = input("Give me some money: ")
print("here is your money", money)

first_money = input("Taka de: ")
second_money = input("A taka de naile gairalamu: ")

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
