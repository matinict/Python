# WHILE LOOP DEMO IN PYTHON
# Demonstrates while loop with three different examples

# EXAMPLE 1 — COUNT FROM 1 TO 5
counter = 1                                # Start at 1
while counter <= 5:                        # Run as long as counter is <= 5
    print(counter)                         # Print the current number
    counter = counter + 1                  # Increment by 1

# EXAMPLE 2 — COUNTDOWN FROM 5
count = 5                                  # Start at 5
while count > 0:                           # Run as long as count is > 0
    print(count)                           # Print the current number
    count = count - 1                      # Decrement by 1

# EXAMPLE 3 — SUM OF FIRST 5 NUMBERS
number = 1                                 # Start at 1
total = 0                                  # Track the running sum
while number <= 5:                         # Run as long as number is <= 5
    total += number                        # Add current number to total
    number += 1                            # Increment by 1
print("Sum is: ", total)                   # Final sum output
