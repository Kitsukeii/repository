age = int(input("How old are you? "))
if age >= 18:
    print("Congratulations, in the UK you're classed as an adult!")
elif age in range(16,18):
    print("You're almost an adult!")
else:
    print("Sorry you're too young, please leave.")