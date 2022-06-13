#COIN FLIP SIMULATION
from random import choice

addFlips = 0
for i in range(10):
	faceHolder = []
	face = True
	while face :
		coinFace = choice(['H', 'T'])
		faceHolder.append(coinFace)
		flips = ''.join(str(a) for a in faceHolder)
		if ('HHH' in flips) or ('TTT' in flips):
			face = False
	flipNo = len(flips)
	print(f'{i+1}. {flips} ({flipNo} trials)')
	
	addFlips += flipNo

print(f'on average, {addFlips/10} flips were needed')

	