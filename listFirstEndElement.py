
##List First-Ends Elements:		
## Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
## makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
## Concepts to practice
## Lists and properties of lists
## List comprehensions (maybe)
## Functions		
	
 def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

##>>> list_end([5, 10, 15, 20, 25])
