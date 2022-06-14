print('conversion from decimal to fraction'.upper())
while True:
	try:
		no = float(input('\nenter number >>> '))
		if no == 0:
			print('0 is 0/1 in fraction')
			continue	
	except: print('must be a number or decimal no')
	else: break
def decimalConverter():
	a = str(no)
	dot = a.index('.')
	l = []
	
	for i in a[dot+1:]:
		l.append(i)
	n = len(l)
	global l1,l2
	l1, l2 = [int(no * (10 ** n))], [int(10 ** n)]
	
	for n in range(2, l1[0]+1):
		while (l1[0] % n == 0) and (l2[0] % n == 0):
			x,y = l1[0]/n, l2[0]/n
			l1.pop(0)
			l2.pop(0)
			l1.append(int(x))
			l2.append(int(y))

decimalConverter()
		
print(f'{no} is  {l1[0]}/{l2[0]} in fraction')
		
		