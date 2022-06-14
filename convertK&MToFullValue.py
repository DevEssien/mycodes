#convert in K and V to full value
import string

val = input('enter value >>> ')

def unitConvert(value):
	v = str(value)
	valueList = [i for i in v if i in list(string.digits)]
	stR = ''.join(str(e) for e in valueList)
	inT = int(stR)
		
	for j in v:
		if j in ('k', 'K'):
			fullValue = inT * 1000
		elif j in ('m', 'M'):
			fullValue = inT * 1000000
			
	return fullValue
	
c = unitConvert(val)
print(c)