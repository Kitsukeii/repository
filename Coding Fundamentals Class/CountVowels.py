word = input("Input your desired word: ")
counter = 0
i = 0
while i < len(word):
    if word[i] == "a":
        counter += 1
    if word[i] == "e":
        counter += 1
    if word[i] == "i":
        counter += 1
    if word[i] == "o":
        counter += 1
    if word[i] == "u":
        counter += 1
    i += 1
print("Out of ", len(word), "letters,", counter, "of them were vowels :) ")