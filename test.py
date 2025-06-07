score = int(input("Give me the student's score: "))
if 90 <= score <= 100:
    print("The grade is A")
elif 80 <= score <= 89:
    print("The grade is B")
elif 70 <= score <= 79:
    print("The grade is C")
elif 60 <= score <= 69:
    print("The grade is D")
elif 50 <= score <= 59:
    print("The grade is E")
elif 40 <= score <= 49:
    print("The grade is E-")
else:
    print("The grade is F or Fail")
