#GRAB CONSECUTIVE INTEGERS
import string
from re import findall

exp = "BARN*21+77-48*CDAIRY87+56-12"

#METHOD1
'''if element is not digit or in s replace with (' ')'''
c = ''.join(' ' if not i.isdigit() else i for i in exp) 
x = c.strip()
y = x.split()
print(y)
		

#METHOD2
x = findall('[0-9]+', exp)
print(x)
