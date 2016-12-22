## Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

## Remember the rules:
## Rock beats scissors
## Scissors beats paper
## Paper beats rock
def compGame():
	import sys
	user1 = input("What's your name?: ")
	user2 = input(" And your name?: ")
	u1 =input("%s, do yo want to choose rock,paper or scissors?: " % user1)
	u2 =input("%s, do yo want to choose rock,paper or scissors?: " % user2)
	
	if u1 == u2:
		return("It's a tie!")
	elif u1=='rock':
		if u2=='scissors':
			return('Rock Wins!')
		else:
			return("Paper wins!")
	elif u1=='scissors':
		if u2=='paper':
			return('scissors Wins!')
		else:
			return("rock wins!")
	elif u1=='paper':
		if u2=='rock':
			return('Paper Wins!')
		else:
			return("scissors wins!")
	else:
		return("Invalid input!! you have not entered rock,paper or scissors,Try again. ")
	sys.exit()
##compGame()
