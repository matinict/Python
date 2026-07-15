
# Python for AI Coding: From Beginner to LLM Engineer
# 3. elif_statement

score = 45                     # Assigns the value 45 to variable score

if score >= 90:                # Checks if score is 90 or more
    print("Grade A")           # Prints Grade A if the condition is True
elif score >= 75:              # Checks if score is 75 or more (if previous condition was False)
    print("Grade B")           # Prints Grade B if this condition is True
elif score >= 50:              # Checks if score is 50 or more
    print("Grade C")           # Prints Grade C if this condition is True
else:                          # Executes if all previous conditions are False
    print("Fail")              # Prints Fail because 45 is less than 50

role = "guest"                 # Assigns the string "guest" to variable role

if role == "admin":            # Checks if role is exactly equal to "admin"
    print("Welcome, Admin!")   # Prints if the role matches "admin"
elif role == "editor":         # Checks if role is exactly equal to "editor"
    print("Welcome, Editor!")  # Prints if the role matches "editor"
elif role == "viewer":         # Checks if role is exactly equal to "viewer"
    print("Welcome, Viewer!")  # Prints if the role matches "viewer"
else:                          # Executes if the role does not match any of the above
    print("Unknown role")      # Prints this because "guest" is not admin, editor, or viewer


 
