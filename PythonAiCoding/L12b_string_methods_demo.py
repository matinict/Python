# Python for AI Coding: From Beginner to LLM Engineer
# STRING METHODS DEMO IN PYTHON
# Demonstrates common built-in string methods:
# lower(), upper(), strip(), replace(), split()


# EXAMPLE 1 - lower() METHOD
# lower
original = "Hello World"                    # creates a string variable with mixed case text
lowered = original.lower()                  # converts all characters to lowercase
print("Lowercase: ", lowered)               # prints the lowercase version: hello world


# EXAMPLE 2 - upper() METHOD
# upper method
uppered = original.upper()                  # converts all characters to uppercase
print("Uppercase: ", uppered)               # prints the uppercase version: HELLO WORLD


# EXAMPLE 3 - strip() METHOD
# strip() method
messy = "   Python   "                      # creates a string with extra spaces around it
cleaned = messy.strip()                     # removes leading and trailing whitespace
print("After strip: ", cleaned)             # prints the cleaned string: Python


# EXAMPLE 4 - replace() METHOD
# replace() method
text = "Java is powerful"                   # creates a string containing the word "Java"
updated = text.replace("Java", "Python")    # replaces "Java" with "Python" in the string
print("After replace: ", updated)           # prints the updated string: Python is powerful


# EXAMPLE 5 - split() METHOD
# split() method
sentence = "Python is easy to learn"        # creates a full sentence as a string
words = sentence.split()                    # splits the string into a list of words
print("Split result: ", words)              # prints the list: ['Python', 'is', 'easy', 'to', 'learn']
