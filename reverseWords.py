## Reverse Word Order 
## Write a program (using functions!) that asks the user for a long string containing multiple words.
## Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
##  My name is Michele Then I would see the string:   Michele is name My shown back to me.

 def reverseWords():
	words = input("Enter your sentence: ") 	
	return ' '.join(words.split()[::-1])

## reverseWords()
## Enter your sentence: I am matin Rahman , Python Developer
## 'Developer Python , Rahman matin am I'
