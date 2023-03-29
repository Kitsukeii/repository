# length = int(input("Length: "))
# width = int(input("Width: "))

# print("Perimiter is: ", (width * 2) + (length * 2))
# print("area is: ", width * length)

# Different ways of storing Data

# ---Lists - Ordered, mutable, collection of values.
#Multiple values contained in a single variable, defined by square brackets with commads [,].
colours - ["blue", "red", "green", "yellow"]
print(colours)

#Referencing - elements in a litst are referenced by their position (or index) this starts from 0, backwards would be -1.

print(colours[0])
print(colours[-4])

#Sub-list of items by slicing, up to but not including the second number.

print(colours[0:2])
print(colours[1:])

#Altering lists using index and new value, delete with del keyword
food = ['bread', 'cheese', 'pasta', 'apple']
food[8] = "rice"
del food[2]
print(food)

#Checking if an item is in a list
print("bread" in food)
print("orange" in food)

#Nested lists
numbers = [1, 2, 3, 4]
letters = ["a", "h", "c", "d"]
combined = [numbers, letters]
print(combined[0][1], combined[1][1])

#Lists can contain multiple data types
my_list = ["red", 5, ["green", "apple"], 10]
print(my_list)

#List methods
my_fruits = ["apple", "orange", "kiwi"]
my_fruits.append("pear")
print(my_fruits)

#Remove
my_fruits.remove("apple")
print(my_fruits)

#Insert
my_fruits.insert(0, "mango")
my_fruits.inset(1, "melon")
print(my_fruits)

#Extend with a list
my_fruits.extend(["grape", "cherry"])

#Join
x = ", ".join(my_fruits)



# ---Dictionairies - unordered, mutable, collection of key-value pairs.
#Similar to list but no index.
#Keys have to be unique, values don't
drinks = {"fizzy": "Sprite", "still": "water", "juice": "orange", "alcoholic":"beer"}
print(drinks)
print(drinks["still"])
#Can only query keys not values

#Add an item
drinks["non-alcoholic"] = "water"
print(drinks)

#Overwrite

drinks["non-alcoholic"] = "squash"
print(drinks)

#Return all keys or values
print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())
print("still" in drinks)

#Get method - returns the value for key else defaults
print(drinks.get("still", "not-found"))
print(drinks.get("stille", "not-found"))
print(drinks.get("stille"))

#Update
drinks.update({"sugary": "cola"})
print(drinks)
#Or
drinks.update(very_sugary = "red-bull")
print(drinks)
#Pop
print(drinks.pop("non-alcoholic"))
print(drinks)
print(drinks.pop("non-alcoholic". "not-found"))
print(drinks)


# Tuple - ordered, ummutable, collection of values.


# Sets - unordered, mutable, collection of unique values. 
