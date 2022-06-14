#fibonacci series 2, using while loop as loop :)

inPut2 = int(input('enter length of fibonacci series >>> '))
def fibonacci(inPut):
	a, b = 0, 1
	loop = 0
	while loop < inPut:
		yield a
		new_b = a+b
		a = b
		b = new_b
		loop += 1
fib = fibonacci(inPut2)

for num in fib:
	print(num)