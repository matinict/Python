###Guessing Game One Solutions

## Generate a random number between 1 and 9 (including 1 and 9).
## Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
## (Hint: remember to use the user input lessons from the very first exercise)
## Extras:
## Keep the game going until the user types “exit”
## Keep track of how many guesses the user has taken, and when the game ends, print this out.

>>> def guessingGame1():
	import random
	number = random.randint(1,9)
	guess = 0
	count = 0
	while guess !=number and guess !="exit":
		guess = input("What your guess?: ")
		if guess == "exit":
			break
		guess = int(guess)
		count += 1
		if guess <number:
			print("Too Low!")
		elif guess >number:
			print("Too high!!")
		else:
			print("You got It!!")
			print(" And it only took you",count,"tries!")

			
##>>> guessingGame1()
##What your guess?: 1
##Too Low!
## What your guess?: 9
## Too high!!
## What your guess?: 1
## Too Low!
## What your guess?: 0
## Too Low!
## What your guess?: 9
## Too high!!
## What your guess?: 7
## You got It!!
## And it only took you 6 tries!
