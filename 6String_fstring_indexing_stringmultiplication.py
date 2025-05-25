vee1 = 'this is a single quote string, "Wow"'
vee2 = "this is vee's double quote string with apostrophe ' "
vee3 = """This is a multiple lines triple quote string.
SO, there are 3 types of string implementation mainly.
We use the single quote when we need to use double quotes in our string,
We use the double quote when we need to use single quote in our string.
"""

print(vee1)
print(vee2)
print(vee3)

# String is immutable, we can't change the string directly.
# my_word = "hello"
# This will cause an error!
# my_word[0] = 'H'

my_word = "hello"
new_word = (
    "H" + my_word[1:]
)  # We take "H" and add the rest of my_word ("ello"), this will work.
print(new_word)  # Output: Hello
print(my_word)  # Output: hello (the original is unchanged)


# Why immutability?
# 1. Copying & sharing: if it were mutable, after doing str2 = str1, if we change one, other one will get changed too.
# 2. Immutability ensures String's hash value never changes
# 3. Security and Predictability: When you pass a string to a function, you know that function can't change your original string. This can make programs easier to reason about and less prone to bugs where data is unexpectedly modified.
# 4. suppose, a string a = "vee", b = "vee". they both are pointing to "vee" but from different places of the code. this is string interning, and only possible because of immutability. And how does it help?? It saves space.

# extras:
greet = "Hi "
repeated_greet = greet * 3  # Creates a new string "Hi Hi Hi "
print(repeated_greet)


# python supports negative indexing as well
negid = "PYTHON"
print(negid[-1])

"""
Character:         P   Y   T   H   O   N
Positive Index:    0   1   2   3   4   5
Negative Index:   -6  -5  -4  -3  -2  -1

"""


# f-string (formatted string literal)
my_string = "PYTHON"
last_char = my_string[-1]  # Accesses the last character
second_last_char = my_string[-2]  # Accesses the second-to-last character

print(f"The last character is: {last_char}")  # Output: N
print(f"The second-to-last character is: {second_last_char}")  # Output: O

