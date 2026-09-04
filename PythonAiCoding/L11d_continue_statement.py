# Python for AI Coding: From Beginner to LLM Engineer
# CONTINUE STATEMENT DEMO IN PYTHON# Description: Demonstrates 
# EXAMPLE 1 — CONTINUE STATEMENT IN FOR LOOP
# ===============================================
fruits = ["apple", "banana", "cherry", "date"]   # creates a list containing four fruit names

for fruit in fruits:                             # loops through each fruit in the list
    if fruit == "banana":                        # checks if the current fruit is "banana"
        continue                                 # skips the current iteration when fruit is "banana"
    print(fruit)                                 # prints all fruits except "banana"


# ===============================================
# EXAMPLE 2 — CONTINUE STATEMENT IN WHILE LOOP
# ===============================================
i = 0                                            # initializes variable i with value 0
while i < 5:                                     # loop runs as long as i is less than 5
    i += 1                                       # increments i by 1 at the start of each iteration
    if i == 3:                                   # checks if i has reached the value 3
        continue                                 # skips the print statement when i equals 3
    print(i)                                     # prints the value of i (except when i is 3)
