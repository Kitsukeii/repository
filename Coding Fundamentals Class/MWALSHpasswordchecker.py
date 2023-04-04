with open("Ignore\common_passwords.txt") as file:
    common_passwords = file.read().splitlines()

    while True:
        password = input("Enter a password to check its strength (type 'quit' to exit): ")
        if password == "quit":
            break
        if password in common_passwords:
                print("Password is a common password. Choose a stronger one.")
                continue
        score = 0
        length = len(password)
        if length >= 8:
            score += 1   
        if any(char.isupper() for char in password):
            score += 1  
        if any(char.islower() for char in password):
            score += 1   
        if any(char.isdigit() for char in password):
            score += 1    
        if any(char in "!@#$%^&*()-+?_=,<>/;" for char in password):
            score += 1

        if score == 5:
            print("Password strength: Very Strong")
        elif score == 4:
            print("Password strength: Strong")
        elif score == 3:
            print("Password strength: Medium")
        elif score == 2:
            print("Password strength: Weak")
        else:
            print("Password strength: Very Weak")