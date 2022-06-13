import string

txT = open('/storage/emulated/0/essienPythonCode/test.txt', 'r')
texT = txT.read()

#METHOD 1. most efficient. 
#for files too
text = texT.split()
count = len(text)
print(f'There are {count} words in the text file')


#METHOD 2. 
#this code doesn't work on files. only strings'
texT = 'Learn by examples! This tutorial supplements all explanations'
text = texT.strip(' .,')
if len(text) > 0:
	count = 1
	for i,e in enumerate(text):
		if e== ' ':
			count += 1
		if text[i]==' ' and text[i+1]==' ':
			count -= 1
else:
	count = 0			
print(f'There are {count} words in the text')

