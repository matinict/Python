
# Python for AI Coding: From Beginner to LLM Engineer



# 5 match case switch-case
day = input("enter a day: ").capitalize()    # Takes day input and capitalizes the first letter
match day:                                   # Starts match-case block to check the value of day
    case "Monday"|"Tuesday"|"Wednesday"
    |"Thursday"|"Friday":                    # Matches any weekday using OR pattern
        print("It's a weekday.")             # Prints if the day is a weekday
    case "Saturday" | "Sunday":              # Matches Saturday or Sunday
        print("It's a weekend!")             # Prints if the day is a weekend
    case _:                                  # Default case if no match is found
        print("Invalid a day.")              # Prints if the input is not a valid day
# calculator using match-case stat
num1 = int(input("Enter first number: "))    # Takes first number input and converts to integer
num2 = int(input("Enter second number: "))   # Takes second number input and converts to integer
operation = input("operation (+, -, *, /):") # Takes the operation symbol as input
match operation:                             # Starts match-case block to check the operation
    case "+":                                # Matches if operation is addition
        print("Result: ", num1 + num2)       # Prints the sum of num1 and num2
    case "-":                                # Matches if operation is subtraction
        print("Result: ", num1 - num2)       # Prints the difference of num1 and num2
    case "*":                                # Matches if operation is multiplication
        print("Result: ", num1 * num2)       # Prints the product of num1 and num2
    case "/":                                # Matches if operation is division
        print("Result: ", num1 / num2)       # Prints the quotient of num1 divided by num2
    case _:                                  # Default case if no valid operation is entered
        print("Invalid operation")           # Prints if the operation is not +, -, *, or /


==
