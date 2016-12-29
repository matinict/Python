## hv problem

def createWriteReadFile():
	import os
	##Create
	os.mknod("newfile.txt")
	f=open("newfile.txt","w")
	f.write("I am learnning Python Programming!!")
	f.close
	f=open("newfile.txt","r")
	print(f.read())
	f.close

	
##>>> createWriteReadFile()
