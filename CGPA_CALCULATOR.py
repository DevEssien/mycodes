#my personal project1
#CGPA calculator

print("CALCULATE YOUR CGPA FOR THE YEAR".center(20))
print()

name = input('Name of student: ')
print()

print('FIRST SEMESTER')

def gpa():
	while True:
		try:
			no_of_courses = int(input("enter number of courses >>>  "))
			if 0 < no_of_courses <= 12:
				pass
			elif no_of_courses == 0:
				print('number must be greater than 1')
				continue
			elif no_of_courses >= 13:
				print('number must be less than 13')
				continue		
		except ValueError:
			print('please enter a number')
		else:
			break
		
	if 0 < no_of_courses <= 12:
		empty_list1 = []
		empty_list2 =[]
		for no in range(1, no_of_courses +1):
			print(input(f'enter course{no} name: '))
			while True:
				try:	
					credit_unit = int(input('enter credit unit >>> '))
					if 0 < credit_unit <= 6:
						pass
					else:
						print('credit unit must be a maximum of 6 and a minimum of 1')
						continue						
				except:
					print('credit unit  must be an integer(digit) not a letter or symbol')
				else:
					break
		
			while True:			
				try:
					grade = str(input('enter grade: ')).lower()
					if grade not in ('a', 'b', 'c', 'd', 'e', 'f'):
						print('grade must be a or b or c or d or e or f')
						continue
				except:
					print('grade must be a string(letter)')
				else:
					break
			
			if 'a' in grade: grade = 5
			elif  'b' in grade: grade =4
			elif 'c' in grade: grade = 3
			elif  'd' in grade: grade =  2
			elif  'e' in grade: grade =1
			elif  'f' in grade: grade = 0
			
			empty_list2.append(credit_unit)
			empty_list1.append(credit_unit * grade)
		print()
			
	global count1	
	count1 = 0
	for num in empty_list1:
		count1 += num
	
	global count2	
	count2 = 0
	for numb in empty_list2:
		count2 += numb
			
gpa()
	
calculation1 = count1/count2

print(f"{name}, your GPA for first semester is {calculation1:.2f}")
print()

print('SECOND SEMESTER')
gpa()

calculation2 = count1/count2
print(f"your GPA for second semester is {calculation2:.2f}")

calculation = (calculation1 + calculation2)/2

print()
print(f"{name}, now  your CGPA for this year(level) is {calculation:.2f}")

if calculation >= 4.5:
	print('you are a first class student. Excellent!!!')
elif 3.5<= calculation < 4.5:
	print('you are a second class upper student. great work, \nyou just need extra efforts to hit the bulls eye')
elif 3.0<= calculation < 3.5:
	print('you are a second class lower student, nice trying but u need to try harder')
elif 2.5<= calculation < 3.0:
	print('you are a third class student, you need to increase your stives')
elif 2.0 <= calculation < 2.5:
	print('you are just a pass student, you need serious work to move up')
