grade = int(input("Enter the grade: "))
if grade > 100 or grade < 0:
    print("The grade is wrong!!")
    exit()


if grade >= 90 and grade <= 100:
    print("Your grade is A ")
elif 80 <= grade <= 89:
    print("Your grade is B")
elif 70 <= grade <= 79:
    print("Your grade is C")
elif 60 <= grade <= 69:
    print("Your grade is D")
elif 50 <= grade <= 59:
    print("Your grade is E")
else:
    print("Your grade is F")

