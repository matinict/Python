# Python for AI Coding: From Beginner to LLM Engineer
# F-STRING DEMO IN PYTHON
# Demonstrates string formatting techniques:
# 1. Old-style concatenation using +
# 2. format() method
# 3. Modern f-strings (formatted string literals)
# Variables used in all examples
name = "Matin"                                            # creates a string variable with the name
age = 25                                                 # creates an integer variable with the age
# METHOD 1 - String concatenation using + operator
print("My name is " + name + " and I am " + str(age) + " years old.")
# joins strings using + and converts age to string with str()
# METHOD 2 - Using the format() method
print("My name is {} and I am {} years old.".format(name, age))
# {} are placeholders that get replaced by values passed to format()
# METHOD 3 - f-string (formatted string literal)
print(f"My name is {name} and i am {age} years old")
# f before the string allows direct variable insertion inside {}
# f-string with expressions (arithmetic inside curly braces)
marks = 87                                               # creates an integer variable for marks
print(f"Total marks after bonus is: {marks + 5}")
# f-string evaluates the expression {marks + 5} and prints the result: 92
# f-string with function calls inside curly braces
def get_percentage(marks):                               # defines a function to calculate percentage
    return marks / 100 * 100                             # returns the percentage value

print(f"Percentage is {get_percentage(marks)} percent")
# f-string calls the function and inserts the returned value
