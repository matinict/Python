# Python for AI Coding: From Beginner to LLM Engineer
# User Input Demo - Taking input from the user using input(),
# int(), float(),  boolean comparison

# --- Example 1: Taking a String Input ---
name = input("Enter your name: ")              # Asks the user to type their name and stores it as a string
print("Hello, " + name + "!")                  # Prints a greeting using the entered name
# --- Example 2: Taking an Integer Input ---
age = int(input("Enter your age: "))           # Asks for age and converts the input string into an integer
print("You will be ", age + 1, "next year.")   # Adds 1 to the age and prints the result
# --- Example 3: Taking a Decimal (Float) Input ---
price = float(input("Enter the price: "))      # Asks for a price and converts the input string into a decimal number
discount = price * 0.1                         # Calculates 10% of the price as the discount
print("Discount is: ", discount)               # Prints the calculated discount value
# --- Example 4: Taking a Boolean-like Input (Yes / No) ---
answer = input("Are you a student? yes or no: ") # Asks a yes/no question and stores the answer as a string
is_student = answer == "yes"                     # Compares the answer to "yes" — result is True or False
if is_student:                                   # Checks if is_student is True
    print("welcome student")                     # Runs if the user typed "yes"
else:                                            # Runs if the answer was anything other than "yes"
    print("hello guest")                         # Prints a guest greeting
