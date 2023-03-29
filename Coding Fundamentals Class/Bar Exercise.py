# Three or more Milkshakes
# The list will be displayed every iteration
# Q is to quit and leave
# If he can't pay he's thrown out

wallet = 10
while wallet > 0:
    drinks = {
    1: {"Vanilla Void": "Vanilla", "price": 7.0},
    2: {"Chocolate Rain Tears": "Chocolate", "price": 6.0},
    3: {"Strawberry Seperation": "Strawberry", "price": 6.5},
    4: {"Blue Balls": "Bubblegum", "price": 8},
    5: {"Potnoodle & a W*ffle": "Banana Nut Waffle", "price": 7},
}
    print("You have ", wallet, "left")
    print("The menu reads:", drinks)
    choice = (input("The barman asks 'What can I fix you?': "))
    if choice == "1":
        wallet -= 7
    elif choice == "2":
        wallet -= 6
    elif choice == "3":
        wallet - 6.5
    elif choice == "4":
        wallet - 8
    elif choice == "5":
        wallet - 7
    elif choice == "Q":
        print("You stand up and leave this poor excuse of a bar")
        exit()

print("You are thrown out for bein' a filthy povvo")