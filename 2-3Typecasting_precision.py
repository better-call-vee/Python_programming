vee = 45

# Basic Typecastings
x_str = str(vee)  # int to string
x_float = float(vee)  # int to float
x_complex = complex(vee)  # int to complex
x_bool = bool(vee)  # int to bool
x_bytes = bytes(str(vee), "utf-8")  # int to bytes via str
x_list = list(str(vee))  # int to list via str
x_tuple = tuple(str(vee))  # int to tuple via str
x_set = set(str(vee))  # int to set via str

# Float with precision formatting
precise_float = format(x_float, ".2f")  # float with 2 decimal places
precise_float_fstring = f"{x_float:.3f}"  # same using f-string (3 decimal places)

# Print values and types
print("x_str:", x_str, "|", type(x_str))
print("x_float:", x_float, "|", type(x_float))
print("x_complex:", x_complex, "|", type(x_complex))
print("x_bool:", x_bool, "|", type(x_bool))
print("x_bytes:", x_bytes, "|", type(x_bytes))
print("x_list:", x_list, "|", type(x_list))
print("x_tuple:", x_tuple, "|", type(x_tuple))
print("x_set:", x_set, "|", type(x_set))

print("precise_float (2 dp):", precise_float, "|", type(precise_float))
print(
    "precise_float_fstring (3 dp):",
    precise_float_fstring,
    "|",
    type(precise_float_fstring),
)
