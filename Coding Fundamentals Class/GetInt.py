top = 7
bottom = 11
counter = 0
while counter < 3:
    counter += 1
    answer = int(input("Input your guess: "))
    if answer in range(top, bottom):
        print("Congratulations, the top limit was ", top," and the bottom limit was ", bottom," your answer was", answer)
        exit()
    
print(None)