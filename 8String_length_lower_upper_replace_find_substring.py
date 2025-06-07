text = "python is fun"
upper_text = text.upper()
print(f"Original: {text}")  # Output: python is fun
print(f"Uppercase: {upper_text}")  # Output: PYTHON IS FUN


text = "Hello, welcome to the world of Python!"
position1 = text.find("welcome")
print(f"'welcome' found at index: {position1}")  # Output: 7

position2 = text.find("Java")
print(f"'Java' found at index: {position2}")  # Output: -1


sentence = "I like cats. Cats are cool."
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)  # Output: I like dogs. Dogs are cool.


text = "PYTHON IS FUN"
lower_text = text.lower()
print(f"Original: {text}")  # Output: PYTHON IS FUN
print(f"Lowercase: {lower_text}")  # Output: python is fun

text = "python is fun"
upper_text = text.upper()
print(f"Original: {text}")  # Output: python is fun
print(f"Uppercase: {upper_text}")  # Output: PYTHON IS FUN



# Returns True if the string starts with the specified prefix, otherwise returns False.
# same for endswith
filename = "report_final.docx"
is_report = filename.startswith("report_")
print(f"Does '{filename}' start with 'report_'? {is_report}") # Output: True

is_image = filename.startswith("img_")
print(f"Does '{filename}' start with 'img_'? {is_image}")   # Output: False

is_doc = filename.endswith(".docx")
print(f"Does '{filename}' end with '.docx'? {is_doc}") # Output: True


# explore strip, lstrip, rstrip