# Python for AI Coding: From Beginner to LLM Engineer
# STRING METHODS DEMO IN PYTHON
# Demonstrates common built-in string methods:
# lower(), upper(), strip(), replace(), split(),
# find(), title(), capitalize(), startswith(), endswith()
# lower() METHOD
original = "Hello World"                          # creates a string variable with mixed case text
lowered = original.lower()                        # converts all characters to lowercase
print("Lowercase: ", lowered)                     # prints the lowercase version: hello world
# upper() METHOD
uppered = original.upper()                         # converts all characters to uppercase
print("Uppercase: ", uppered)                      # prints the uppercase version: HELLO WORLD
# strip() METHOD
messy = "   Python   "                            # creates a string with extra spaces around it
cleaned = messy.strip()                           # removes leading and trailing whitespace
print("After strip: ", cleaned)                   # prints the cleaned string: Python
# replace() METHOD
text = "Java is powerful"                          # creates a string containing the word "Java"
updated = text.replace("Java", "Python")           # replaces "Java" with "Python" in the string
print("After replace: ", updated)                  # prints the updated string: Python is powerful
# split() METHOD
sentence = "Python is easy to learn"               # creates a full sentence as a string
words = sentence.split()                          # splits the string into a list of words
print("Split result: ", words)                    # prints the list of words
# find() METHOD
text = "Learning Python is fun"                    # creates a new string to search within
position = text.find("Python")                     # finds the starting index of "Python"
print("Found at index: ", position)               # prints the index where "Python" begins
# title() METHOD
heading = "Welcome to Python programming"          # creates a lowercase heading string
formatted = heading.title()                        # capitalizes the first letter of each word
print("Title case: ", formatted)                   # prints title-cased string
# capitalize() METHOD
msg = "hello WORLD"                               # creates a string with mixed casing
cleaned = msg.capitalize()                         # capitalizes only the first letter, rest lowercase
print("capitalize: ", cleaned)                     # prints: Hello world
# startswith() METHOD
greeting = "Hello everyone"                        # creates a greeting string
print(greeting.startswith("Hello"))                # checks if string starts with "Hello" -> True
print(greeting.startswith("Hi"))                   # checks if string starts with "Hi" -> False
# endswith() METHOD
print(greeting.endswith("everyone"))               # checks if string ends with "everyone" -> True
print(greeting.endswith("Hello"))                  # checks if string ends with "Hello" -> False

# end  common built-in string methods:
