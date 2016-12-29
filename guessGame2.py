def guessGame2():
	i = 0;
	#i is lowest number in range of possible guesses
	j=100
	#j is highest number in range of possible guesses
	m=50
	#m is middle number in range of possible guesses
	count=1
	#counter is the number of guesses take
	print("\n Please Guess A Number: ")
	cond = input("Is ur guess " + str(m) + "? (0 means it's too low, 1 means it's ur guess and 2 means it's too high):")
	while cond !=1:
		count += 1
		if cond == 0:
			i = m+1
		elif cond == 2:
			j = m-1
		m = (i+j)/2
		cond = input("Is ur guess " + str(m) + "? (0 means it's too low, 1 means it's ur guess and 2 means it's too high):")
	print("\nIt took" , count , "times to guess your number:\n\n ")

##>>> guessGame2()
