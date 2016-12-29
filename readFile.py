
## Read From File
## Exercise:Given a .txt file that has a list of a bunch of names,
## count how many of each name there are in the file, and print out the results to the screen. 
##I have a .txt file for you, if you want to use it!

def readFile():
	count_dict = {}
	with open('test.txt') as f:
		line = f.readline()
		while line:
			line = line.strip()
			if line in count_dict:
				count_dict[line]+=1
			else:
				count_dict[line] = 1
			line = f.readline()			
		print('\n',count_dict)
## >>> readFile()
