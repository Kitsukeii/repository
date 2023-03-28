print("This is a calculator UwU")
print()
print("Please input your numbers.")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print("What would you like to do with these numbers?")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (x)")
print("4. Divide (➗)")
print("5. Square")
print("6. Exit the calculator")
while True:
    option = int(input("Please type the number of the option you would like to choose: "))
    if option == 1:
        print(num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        print(num1 / num2)
    elif option == 5:
        print(num1 ** num2)
    else:
        print("You have chosen to exit, goodbye :)")
        exit

