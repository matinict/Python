##Ask the user for a string and print out whether this string is a palindrome or not.
##(A palindrome is a string that reads the same forwards and backwards.)
def palindromeTest(word):
	rvs=word[::-1]
	if word ==rvs:
		print("This Word is Palindrome")
	else:
		print("This Word is not Palindrome")

		
##>>> palindromeTest("Matam")
##This Word is not Palindrome
##>>> palindromeTest("matam")
##This Word is Palindrome
