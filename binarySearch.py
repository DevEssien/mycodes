l = [3,2,6,4,0,8,9,3,1,4]
print(l)

def binarySearch(searchList):
	no = int(input('enter no to search >>> '))
	listNo = sorted(searchList)
	midValue = round(len(listNo)/2)

	while no != listNo[midValue]:
		if no < listNo[midValue]:
			del listNo[midValue:]
		elif  no > listNo[midValue]:
			del listNo[:midValue]
		midValue = round(len(listNo)/2)
	else:
		return f'{no} is found' 
		


#	if no != listNo[midValue]:
		#f'{no} is not found' 
print(binarySearch(l))	