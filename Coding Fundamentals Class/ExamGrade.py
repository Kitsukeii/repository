print("Exam Grade Sheet")
print()
level = int(input("Please input your exam level: "))
grade = int(input("Please inpute your score: "))
if level == 1:
    if grade in range(71,101):
        print("Distinction")
    elif grade in range(61,71):
        print("Merit")
    elif grade in range(50,61):
        print("Pass")
    elif grade in range(1,50):
        print("Fail")
    elif grade < 1:
        print("Invalid score")
    elif grade > 100:
        print("Invalid score")
if level == 2:
    if grade in range(66,101):
        print("Distinction")
    elif grade in range(51,66):
        print("Merit")
    elif grade in range(40,51):
        print("Pass")
    elif grade in range(1,40):
        print("Fail")
    elif grade < 1:
        print("Invalid score")
    elif grade > 100:
        print("Invalid score")
