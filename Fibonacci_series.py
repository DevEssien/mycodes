#code to print all the fibonacci series in a specified number 

no = int(input('no: '))

def fibonacci_series(no):
	this_list= [0,1]
	for i in range(1, no+1):
		calc = this_list[-1] + this_list[-2]
		this_list.append(calc)

	string_ = ", ".join(str(i) for i in this_list)
	print(string_)
	
fibonacci_series(no)
		
		