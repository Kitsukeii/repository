def average():
    while True:
        mark1 = int(input("Your first score: "))
        if mark1 in range(0,101):
            break

    while True:
        mark2 = int(input("Your second score: "))
        if mark2 in range(0,101):
            break
    while True:
        mark3 = int(input("Your third score: "))
        if mark3 in range(0,101):
            break
    average = (mark1 + mark2 + mark3) / 3
    print("Your average score is: ", average)
    if average >= 65:
        print("You have passed")
    if average < 65:
        print("You have failed, try again next time")

print("Please input your Maths scores")
average()

print("Please input your English scores")
average()

print("Please input your ICT scores")
average()