# syntax: my_string[start:stop:step]
"""
start: The index where the slice begins (inclusive). If omitted, it defaults to the beginning of the string (index 0).

stop: The index where the slice ends (exclusive). This means the character at the stop index is not included in the slice. If omitted, it defaults to the end of the string.

step: An optional argument that determines the increment of the slice. If omitted, it defaults to 1 (meaning take every character).
"""

# from "TANVEE",
# to get "VEE":
word = "TANVEE..LESSGO"
slice1 = word[3:6]  # Start at index 3, go up to (but not including) index 6
print(slice1)  # Output: VEE

lessgo = word[8:]  # starting till the end
print(lessgo)

tanvee = word[:6]  # go up to 6 from the starting without including 6
print(tanvee)

word = "PYTHON"
slice5 = word[::2]  # No start, no stop, just a step of 2, every second letter
print(slice5)  # Output: PTO (P at 0, T at 2, O at 4)


# Reverse a string using negative step trick
reversed_word = word[::-1]  # No start, no stop, step by -1 (go backwards)
print(reversed_word)  # Output: NOHTYP


"""
If your start or stop indices are out of bounds, Python is quite forgiving and won't usually raise an error; 
it'll just give you what it can. For example, word[0:100] on "PYTHON" will just give you "PYTHON".
"""

word = "Always look on the bright side of life."
print(word[:25:-1])  # reverse from back
