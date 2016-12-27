##Ask the user for a number and determine whether the number is prime or not.
##(For those who have forgotten, a prime number is a number that has no divisors.).
##You can (and should!) use your answer to  Take this opportunity to practice using functions, described below.

def primeChk(number):	
	num = int(number)
	a = [x for x in range(2,num) if num % x ==0]
	print ("The value of a is: ", a)
	
	if num > 1 :
		if len(a)== 0:
			print ("Prime")
		else:
			print("Not Prime")
	else:
		print("Not Prime")
