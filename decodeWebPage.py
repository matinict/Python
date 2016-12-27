## Decode A Web Page
## My sincerest apologies for being late in posting these exercises.
##  My boyfriend came to visit me in Jerusalem for the last two weeks, so I haven’t had any spare cycles to tackle the Python problems.
## I should learn to write a few in advance in case I am ever put in this kind of situation again.
## In any case, this exercise should make up for the lack of exercises the last few weeks - it’s a fun one.
## This is a slightly longer and more involved exercise than many previous ones, so I will not post the solution for two weeks, but I will post a new exercise next week. Enjoy!

def decodeWebPage():
	import requests
	from bs4 import BeautifulSoup
	base_url=input('Enter Url(ex. http://www.nytimes.com): ')
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text)	
	for story_heading in soup.find_all(class_= {'story-heading','default'}):
		if story_heading.a:
			print(story_heading.a.text.replace("\n"," ").strip())
		else:
			print (story_heading.content[0].strip())
			
## >>> decodeWebPage()
## Enter Url(ex. http://www.nytimes.com): http://bangla.bdnews24.com
