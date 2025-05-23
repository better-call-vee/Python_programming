user_input = input("Enter a number: ")
a = int(user_input)

if a > 5:
    print("Greater than 5")
elif a == 5:
    print("Equals to 5")
else:
    print("Less than 5")

user_input2 = input("Enter True or False: ")
boss = user_input2.lower() == "true"

if boss is True:  # or if boss:
    print("Tel er bakso niye astesi, boss re tel dibo")
else:
    print("lunch er pore asen")


user_input3 = input("Enter True or False: ")
boss = user_input3.lower() == "true"

if not boss:
    print("lunch er pore asen")
else:
    print("Tel er bakso niye astesi, boss re tel dibo")

# nested conditions
if boss:
    print("Boss you are joss")
    coin = input("Enter Your Choice: ")
    if coin == "tail":
        print("batting")
    else:
        print("bowling")
else:
    print("You're loss not a boss")


if a > 3 and boss:
    print("The number is greater than 3 and you are the boss")
else:
    print("Either the number is less than or equal to 3 or you are not the boss")

if a > 10 or boss:
    print("Either the number is greater than 10 or you are the boss")
else:
    print("The number is less than or equal to 10 and you are not the boss")
