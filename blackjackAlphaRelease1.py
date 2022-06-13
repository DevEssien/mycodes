#VARIABLE DEFINITIONS
# listOfHands = lh
# noOfHands = h
# noOfCardsPerHand = c
# firstIndexOfLastIndex_In_lh = f
# listOfPoints = lR

import time
from random import choice, randrange
noOfHands = int(input('enter no of players >>> '))
h= noOfHands +1
#h= 2
c = 2

def createDeck():
	global listOfCards
	listOfCards = []
	for suit in ['s','h','d','c']:
		for value in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
			listOfCards.append(value+suit)
	return listOfCards, len(listOfCards)
createDeck()


def shuffle(lisT):
	for i in range(0, len(lisT)):
		randInd = randrange(i, len(lisT))
		lisT[i], lisT[randInd] = lisT[randInd], lisT[i]
	return lisT
d = shuffle(listOfCards)

lh = [[] for times in range(h)]

for num in range(c):
	for ind in range(h):
		lh[ind].append(d.pop(0))


f =  [lh[-1][1]]
cardDealt=  lh[:len(lh)-1]  +  [f]
print(f'cards dealt \n>>>{cardDealt}')

def valueOfAce():
	start = True
	while start:
		global aceValue
		aceValue = input(f'player{ind+1} decide Ace value  or s to split cards\nAceCard>>> ').lower()
		if aceValue not in ('1','11'):
			print('decide either 1 or 11')
			continue
		else: 
			start = False			

def valueOfAce2():
	start = True
	while start:
		global aceValue
		aceValue = input(f'player{ind+1} decide Ace value\nAceCard>>> ').lower()
		if aceValue not in ('1','11'):
			print('decide either 1 or 11')
			continue
		else: 
			start = False	

lP = []
cardValue=[[] for t in range(len(lh))]

		
def calculateCardPoint():
	for ouTer in cardValue:
		addCard = 0
		for inNer in ouTer:
			addCard += inNer
		lP.append(int(addCard))

def pointList():
	global l
	l = []
	for i in lh:
		sh = ''.join(str(b) for b in i)
		l.append(sh)
	
	global ind
	global inD
	for ind,outer in enumerate(l[:-1]):
		for inD, inner in enumerate(outer):
			if inner[0] in ('2','3','4','5','6','7','8','9'):
				cardValue[ind].append(int(inner[0]))
			if inner in ('1','Q','K','J'):
				cardValue[ind].append(10)
			if inner == 'A'  :
				if l[ind][:3].count('A') == 2:
					valueOfAce() #Calling the ace decision function
					if aceValue == '1':
						cardValue[ind].append(1)
					elif  aceValue == '11':
						cardValue[ind].append(11)
					if aceValue in ('split', 's'):
						pass
						'''print('splits..')
						cardValue[ind].append(8)'''
				elif l[ind][:3].count('A') == 1:
					valueOfAce2() #Calling the second ace decision function
					if aceValue == '1':
						cardValue[ind].append(1)
					elif  aceValue == '11':
						cardValue[ind].append(11)
	
	for outer in l[-1]:
		for inner in outer:
			if inner[0] in ('2','3','4','5','6','7','8','9'):
				cardValue[-1].append(int(inner[0]))
			if inner in ('1','Q','K','J'):
				cardValue[-1].append(10)
			if inner == 'A'  :
				if l[-1].count('A') == 2:
					cardValue[-1].append(6)# 6+6 = 12. so dealer gets soft 12 with 2Ace
				elif l[-1].count('A') == 1:
					cardValue[-1].append(11) #returns once for 1 Ace	
	
	calculateCardPoint()	
pointList()

def noneAce():
	if newCard[0] in ('2','3','4','5','6','7','8','9'):
		cardValue[num].append(int(newCard[0]))
	if newCard[0] in ('1','J','Q', 'K') :
		cardValue[num].append(10)


def valueOfAce3():
	start = True
	while start:
		global aceValue
		aceValue = input(f'decide Ace value\nAceCard>>> ').lower()
		if aceValue not in ('1','11'):
			print('decide either 1 or 11')
			continue
		else: 
			start = False	

def ace():
	valueOfAce3()
	cardValue[num].append(int(aceValue))
		
	
  #PLAYER NEW CARD REQUEST PLAY
for num in range(len(lP) - 1):
	qualified = True
	while qualified:
		print(f'\nplayer{num+1} \nFace of your cards {lh[:][num]} \nyour card point is  {lP[num]}')
		if lP[num] == 21:
			print('BLACKJACK!!!')
			break
		else:
			question = input('Enter \'hit\'  to receive another card from deck or  \'stand\' to stay with just your card \n>>> ').lower()
			if question in ('hit', 'h', 'yes', 'y') :
				newCard = d.pop(0)
				lh[num].append(newCard)
				if newCard[0] != 'A':
					'''clear lP for new append after calc'''
					lP.clear() 
					print(f'take card \'{newCard}\'')
					yourCards = lh[:][num]
					print(f'your hand of cards is {yourCards}')
					noneAce()
					calculateCardPoint()
					print(f'your card point is {lP[num]}')
					if lP[num] > 21:
						print('BUST!!!')
						qualified = False
					elif lP[num] == 21:
						qualified = False
					else: continue	
				else:
					lP.clear()
					#code for ace value decision
					print(f'take card \'{newCard}\'')
					yourCards = lh[:][num]
					print(f'your hand of cards is {yourCards}')
					ace()
					calculateCardPoint()
					print(f'your card point is {lP[num]}')
					if lP[num] > 21:
						print('BUST!!!')
						qualified = False
					elif lP[num] == 21:
						qualified = False
					else: continue	
				continue
			
			elif question in ('stand', 'stay', 's', 'no', 'n') :
				qualified = False

	  	#DEALER
print(f'\nFace of dealer\'s cards \n>>> {lh[-1][:]}\nDealer\'s card point >>> {lP[-1]}')
if lP[-1] == 21:
	print('BLACKJACK!!')
		
	#code for dealer. must be >16
dealerPoint = lP[-1]
while dealerPoint < 17:
	newcard= d.pop(0)
	lh[-1].append(newcard)
	if newcard[0] != 'A':
		lP.clear()
		print('getting dealer a card from deck...')
		time.sleep(2)
		print(f'>>> \'{newcard}\'')
		dealerCards = lh[:][-1]
		print(f'Dealer cards {dealerCards}')
			#condition for values of card
		if newcard[0] in ('2','3','4','5','6','7','8','9'):
			cardValue[-1].append(int(newcard[0]))
		elif newcard[0] in ('1','J','Q', 'K') :
			cardValue[-1].append(10)
		
		calculateCardPoint()
		print(f'Dealer card point is {lP[-1]}')
		if lP[-1] > 21:
			print('BUST!!!')
		dealerPoint = lP[-1]
			
	elif newcard[0] == 'A':
		print('getting a card from deck...')
		#time.sleep(1)
		print(f'>>> \'{newcard}\'')
		dealerCards = lh[:][-1]
		print(f'Dealer cards {dealerCards}')
		      #condition for Ace decision
		if lP[-1]> 10:
			newPoint = lP[-1] +1 
			lP.pop(-1)
			lP.append(newPoint)
			dealerPoint = lP[-1]	
		elif lP[-1] <= 10:
			newP = lP[-1] + 11
			lP.pop(-1)
			lP.append(newP)
			dealerPoint = lP[-1]
						
print(f'\nCard points\n>>> {lP}')
print()


#check win conditions
for index, poinT  in enumerate(lP[:-1]):
	playerNumber = index + 1
	if lP[index] < 21 and lP[-1] < 21:
		if lP[index] > lP[-1]:
			print(f'player{playerNumber} wins in this round')
		elif lP[index] == lP[-1]:
			print(f'player{playerNumber} push this round')
		else:
			print(f'player{playerNumber} lose in this round')
	if lP[index] > 21 and (lP[-1] < 21 or lP[-1]  >21):
		print(f'player{playerNumber} lose in this round')
	if lP[index] < 21 and lP[-1]  >21:
		print(f'player{playerNumber} wins in this round')
	elif lP[index] != 21 and lP[-1]  == 21:
		print(f'player{playerNumber} lose in this round')
	if lP[index] == 21:
		print(f'player{playerNumber} wins in this round')
		
		