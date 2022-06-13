#TWO DICE SIMULATION
from random import choice

def rollDice():
	dice = [1,2,3,4,5,6]
	record = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, '11':0, '12':0}
	for i in range(1000):
		face = str(choice(dice) + choice(dice))
		record[face] += 1
	
	noOfOutcomes = [1,2,3,4,5,6,5,4,3,2,1]
	print('Total : Simulated percent : Expected percent\n')
	
	for total, freq, n in zip(range(2,13), record, noOfOutcomes):
		simulatedPercent =  (record[freq] / 1000) * 100
		expectedPercent = (n / 36) * 100
		print(f'{total} : {simulatedPercent:.2f}  : {expectedPercent:.2f}')
	
rollDice()
