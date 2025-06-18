age = 45 #integer
"""
Though we used to write variable types in C++/C. We don't need to do that in python
"""
interest_rate = 2.5 #float
name = "You can't see me" #string
district = 'Khulna' #string/character

vee = 45
x = str(vee)
print(type(x))

#multiple initialization with comma
x, y, z = 2, 4, "c"
print(y, x)
x, y = 4, "tanvee"

import random
print(random.randrange(1, 10))

z = 1j #complex number
print(z)
print(type(z))
print('\n')

is_single = True
# is_sleeping = False

print(age)
print(district)

#let's explore the types by a syntax
# """  """ we can get the multi lines comment by command alt + shift + a 
# and one line comment Ctrl + /
print(type(age))
print(type(interest_rate))
print(type(name))
print(type(is_single))

print("Tanvee" + " " + "Success" + " " + "Hardwork") #String concatenation
text = f"You can't {age} see me {district}."
print(text) 
