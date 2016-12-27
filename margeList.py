## List Remove Duplicates    
## Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

## Extras: Write two different functions to do this - one using a loop and constructing a list, and another using sets.
## Go back and do Exercise 5 using sets, and write the solution for that in a different function.


 def margeList():
	mylist = input("Enter a list of numbers, SEPERATED by WHITE SPACE(3 5 66 etc.): ")
	# now you can use the split method of strings to get a list
	lst = mylist.split() # splits on white space by default
	newList=[]
	for i in lst:
		if i in newList:
			pass
		else:
			newList.append(i)
	print(newList)

	
## >>> margeList()
