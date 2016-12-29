## Draw A Game Board    
## Exercise:This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
## The other 3 exercises are: Part 2, Part 3, and Part 4.
## Time for some fake graphics! Let’s say we want to draw game boards that look like this:
##  --- --- --- 
## |   |   |   | 
##  --- --- ---  
## |   |   |   | 
##  --- --- ---  
## |   |   |   | 
## --- --- --- 
## This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
## Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
## Remember that in Python 3, printing to the screen is accomplished by

 def drawBoard(squareNum):
	sn = int(squareNum)
	i=0
	ho = "----"
	ve = "|   "	
	ho =ho * sn
	ve = ve * (sn+1)
	print("\nWelcome To Tic Tac Toe GameBoard!! \n")
	while i < sn+1:
		print ("  ",ho)
		if not (i==sn):
			print("  ",ve)
		i+=1

		
##>>> drawBoard()
