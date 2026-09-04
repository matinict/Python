# Python for AI Coding: From Beginner to LLM Engineer
# STRING METHODS DEMO IN PYTHON
# Demonstrates common built-in string methods:
# lower(), upper(), strip(), replace(), split(),
# find(), title(), capitalize(), startswith(), endswith(),
# count(), isalpha(), isdigit(), isalnum(), join()
# lower() method
original = "Hello World"          # creates a string with mixed case text
lowered = original.lower()        # converts all characters to lowercase
print("Lowercase: ", lowered)     # prints: Lowercase:  hello world
# upper() method
uppered = original.upper()              # converts all characters to uppercase
print("Uppercase: ", uppered)           # prints: Uppercase:  HELLO WORLD
# strip() method
messy = "   Python   "                  # creates a string with extra spaces around it
cleaned = messy.strip()                 # removes leading and trailing whitespace
print("After strip: ", cleaned)         # prints: After strip:  Python
# replace() method
text = "Java is powerful"               # creates a string containing the word Java
updated = text.replace("Java", "Python")# replaces Java with Python in the string
print("After replace: ", updated)       # prints: After replace:  Python is powerful
# split() method
sentence = "Python is easy to learn"    # creates a full sentence as a string
words = sentence.split()                # splits the string into a list of words by spaces
print("Split result: ", words)          # prints: Split result:  ['Python', 'is', 'easy', 'to', 'learn']
# find() method
text = "Learning Python is fun"         # creates a string to search within
position = text.find("Python")          # finds the starting index of Python in the string
print("Found at index: ", position)     # prints: Found at index:  9
# title() method
heading = "Welcome to Python programming"         # creates a string in lowercase format
formatted = heading.title()             # capitalizes the first letter of each word
print("Title case: ", formatted)        # prints: Title case:  Welcome To Python Programming
# capitalize() method
msg = "hello WORLD"                     # creates a string with mixed case text
cleaned = msg.capitalize()              # capitalizes only the first character, lowers the rest
print("capitalize: ", cleaned)          # prints: capitalize:  Hello world
# startswith() method
greeting = "Hello everyone"             # creates a greeting string
print(greeting.startswith("Hello"))     # checks if string starts with Hello - prints: True
print(greeting.startswith("Hi"))        # checks if string starts with Hi - prints: False
# endswith() method
print(greeting.endswith("everyone"))    # checks if string ends with everyone - prints: True
print(greeting.endswith("Hello"))       # checks if string ends with Hello - prints: False
# count() method
sentence = """Python is easy.
Python powerful. Python popular.""" # creates a sentence with Python repeated
count = sentence.count("Python")        # counts how many times Python appears in the sentence
print("total count: ", count)           # prints: total count:  3
# isalpha() method
name = "Python"                         # creates a string with only letters
print(name.isalpha())                   # checks if all characters are letters - prints: True

mixed = "Python3"                       # creates a string with letters and a digit
print(mixed.isalpha())                  # checks if all characters are letters - prints: False
# isdigit() method
num = "2025"                            # creates a string containing only digits
print(num.isdigit())                    # checks if all characters are digits - prints: True

bad_input = "year2025"                  # creates a string with letters and digits
print(bad_input.isdigit())              # checks if all characters are digits - prints: False
# isalnum() method
code = "abc123"                         # creates a string with letters and digits (no spaces)
print(code.isalnum())                   # checks if all characters are letters or digits - prints: True

value = "abc 123"                       # creates a string with a space between letters and digits
print(value.isalnum())                  # returns False because space is not alphanumeric
# join() method
words = ["Python", "is", "awesome"]     # creates a list of three words
result = " ".join(words)                # joins the list elements into a single string with spaces
print(result)                           # prints: Python is awesome
