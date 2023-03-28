weight = float(input("Weight of item: "))
unit = input("Unit of weight, lb or kg?: ")

if unit == "kg":
    print("That would be", (weight * 2.2), "lb's")
elif unit == "lb":
    print("That would be", (weight / 2.2), "kg")