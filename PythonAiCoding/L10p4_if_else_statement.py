
# Python for AI Coding: From Beginner to LLM Engineer
# 4. if_else_statement

age = 15                                         # Assigns the value 15 to variable age

if age >= 18:                                    # Checks if the person is 18 years or older
    has_id = False                               # Assigns False to has_id
    if has_id:                                   # Checks whether the person has an ID
        print("You are eligible to vote.")       # Executes if has_id is True
    else:                                        # Executes if has_id is False
        print("You need an ID to vote.")         # Prints this message when ID is missing
else:                                            # Executes if age is less than 18
    print("You must be at least 18 to vote.")    # Prints because age is 15

score = 85                                       # Assigns the value 85 to variable score

if score >= 60:                                  # Checks if the student has passed
    if score >= 80:                              # Checks if the student scored 80 or more
        print("You passed with distinction.")    # Executes because score is 85
    else:                                        # Executes if score is between 60 and 79
        print("You passed.")                     # Prints normal pass message
else:                                            # Executes if score is less than 60
    print("You failed the exam.")               # Prints fail message
