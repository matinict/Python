# Python for AI Coding: From Beginner to LLM Engineer
# ===============================================
# 1. FOR LOOP WITH A LIST
# ===============================================
fruits = ["apple", "banana", "mango"]      # creates a list containing three fruit names
for fruit in fruits:                       # loops through each item in the fruits list
    print(fruit)                           # prints the current fruit in each iteration
# ===============================================
# 2. FOR LOOP WITH range() FUNCTION
# ===============================================
for number in range(1, 6):                 # loops through numbers from 1 to 5
    print(number)                          # prints the current number
# ===============================================
# 3. FOR LOOP WITH A STRING
# ===============================================
text = "Hello World"                       # stores the string "Hello World" in variable text
for letter in text:                        # loops through each character in the string
    print(letter)                          # prints each character one by one
# ===============================================
# 4. BREAK STATEMENT IN FOR LOOP
# ===============================================
fruits = ["apple", "banana", "cherry"]     # creates a new list of fruits
for fruit in fruits:                       # loops through each fruit in the list
    if fruit == "banana":                  # checks if the current fruit is "banana"
        break                              # stops the loop completely when "banana" is found
    print(fruit)                           # prints fruit until the loop breaks
# ===============================================
# 5. CONTINUE STATEMENT IN FOR LOOP
# ===============================================
fruits = ["apple", "banana", "cherry"]     # creates another list of fruits
for fruit in fruits:                       # loops through each fruit in the list
    if fruit == "banana":                  # checks if the current fruit is "banana"
        continue                           # skips the current iteration when fruit is "banana"
    print(fruit)                           # prints all fruits except "banana"
