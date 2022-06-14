#code for fibonacci series using generators

input_ = int(input("enter number: "))

def fib(n):
	start= 0
	stop = 1
	for num in range(input_):
		yield start #yield pauses the iteration
		temp = start
		start = stop #this line holds the new value for the start. its used when the loop runs again
		stop = temp + stop
		
for number in fib(input_):
		print(number)
		
		
fib(input_)