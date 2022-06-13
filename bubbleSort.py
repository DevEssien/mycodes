#BUBBLE SORT ALGORITHM

lisT = [20,3,2,10,7,6,67,26,3,14,4,7,13,3,2,4,0,8,9,6,1,3,1,3,1,4]

def bubbleSort(array):
	for j in (range(len(array)-1)):
		for i in range(len(array)-1):
			if array[i+1] < array[i]:
				array[i], array[i+1] = array[i+1], array[i]
	print(array)		
bubbleSort(lisT)

#note: length of array is reduced in line 6 and 7 by 1 because we must know the second element to compare with the first, so the iteration times is reduced by 1 as we wont have an element(obviously not) after the last element to compare with the last element. so we avoided IndexError