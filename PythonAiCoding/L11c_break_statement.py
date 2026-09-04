# Python for AI Coding: From Beginner to LLM Engineer
# BREAK STATEMENT DEMO IN PYTHON
# Demonstrates how break works inside for loop and while loop


# EXAMPLE 1 - BREAK STATEMENT IN FOR LOOP
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)


# EXAMPLE 2 - BREAK STATEMENT IN WHILE LOOP
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
