## Password Generator        
## Exercise:Write a password generator in Python. Be creative with how you generate passwords - 
## strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
## The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

## Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.	

 def pw_gen():
	import string
	import random	
	size=int(input('How many characters in your password?:'))
	chars=string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(chars) for _ in range(size))

## >>> pw_gen()
## How many characters in your password?:4
## 'y+*U'
