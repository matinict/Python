# Python for AI Coding: From Beginner to LLM Engineer
# REGISTRATION AND LOGIN DEMO IN PYTHON
# Demonstrates user registration and login validation
# using input(), if-else, and string comparison


# REGISTRATION - Collecting user details
username = input("Register a username: ")                 # prompts user to enter a username and stores it
password = input("Register a password: ")                 # prompts user to enter a password and stores it
email = input("Register your email: ")                    # prompts user to enter an email and stores it
print("Registration successful!")                         # confirms that registration is complete


# LOGIN - Verifying user credentials
login_username = input("Enter your username: ")           # prompts user to enter their username for login
login_password = input("Enter your password: ")           # prompts user to enter their password for login

if login_username == username and login_password == password:   # checks if both username and password match
    print("Login successful! Welcome, " + login_username + "!")  # prints welcome message if credentials match
else:                                                     # runs if either username or password is wrong
    print("Login failed. Invalid username or password.")  # prints error message for failed login
