print("Pythagoras calculator!")
print()
a = float(input("Please input the length of A: "))
b = float(input("Please input the length of B: "))
c = float(input("Please input the length of C: "))
print("-----------------------------")
print("1. Calculate A by using B & C")
print("2. Calculate B by using A & C")
print("3. Calculate C by using A & B")
print("-----------------------------")
selection = int(input("Which option would you like to choose?: "))
if selection == 1:
    print((b**2) + (c**2))
elif selection == 2:
    print((a**2) + (c**2))
elif selection == 3:
    print((a**2) + (b**2))