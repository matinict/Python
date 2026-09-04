##L12a_string_demo.py
# Python for AI Coding: From Beginner to LLM Engineer
# STRING DEMO IN PYTHON
# Demonstrates string creation, concatenation, length, indexing, and slicing
# EXAMPLE 1 - CREATING A STRING
greeting = "Hello, Python"                  # creates a string variable named greeting
print(greeting)                             # prints the string value: Hello, Python
# EXAMPLE 2 - STRING CONCATENATION
# concatenation - "Hello" + "World" = "Hello World"
first = "Hello"                             # creates a string variable named first
last = "World"                              # creates a string variable named last
full = first + " " + last                   # joins first, space, and last into one string
print(full)                                 # prints the concatenated result: Hello World
# EXAMPLE 3 - FINDING THE LENGTH OF A STRING
# Uses the built-in function len()
text = "Python Programming"                 # creates a string variable named text
length = len(text)                          # counts the number of characters in text
print("length: ", length)                   # prints the length of the string: 18
# EXAMPLE 4 - ACCESSING CHARACTERS FROM A STRING
text = "Hello"                              # creates a new string named text
first_letter = text[0]                      # accesses the first character (index 0)
print(first_letter)                         # prints the first letter: H
# EXAMPLE 5 - STRING SLICING
# Extract just a part of a string - also called slicing
phrase = "Python is powerful"               # creates a string variable named phrase
part = phrase[0:6]                          # slices characters from index 0 to 5
print(part)                                 # prints the sliced part: Python
