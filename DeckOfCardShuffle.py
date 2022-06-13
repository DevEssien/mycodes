#exercise
from random import choice, randrange

def createDeck():
	global listOfCards
	listOfCards = []
	for suit in ['s','h','d','c']:
		for value in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
			listOfCards.append(value+suit)
	return listOfCards, len(listOfCards)


def shuffle(lisT):
	for i in range(0, len(lisT)):
		randInd = randrange(i, len(lisT))
		lisT[i], lisT[randInd] = lisT[randInd], lisT[i]
	return lisT


def deal(noOfHands, noOfCardsPerHand, deckOfCards):
	listOfHandsDealt = []
	
	for hand in range(noOfHands):
		listOfHandsDealt.append([])
	for card in range(noOfCardsPerHand):
		for hanD in range(noOfHands):
			passCard = deckOfCards.pop(0)
			listOfHandsDealt[hanD].append(passCard)
			
	listOfHandsDealt.extend([deckOfCards])
	return listOfHandsDealt	


print('DECK OF CARDS')	
print(createDeck())

print()
print('SHUFFLED DECK OF CARDS')
print(shuffle(listOfCards))

print()
while True:
	try:
		noOfHands = int(input('enter no of hands >>> '))
		noOfCardsPerHand = int(input('enter no of cards per hand >>> '))
		print()
		if (noOfHands or noOfCardsPerHand) == 0:
			print('number cannot be zero') 
		if (noOfHands * noOfCardsPerHand) <=  52:
			print('LIST OF HANDS DEALT')
			print(deal(noOfHands,noOfCardsPerHand,listOfCards))
		else:
			print('can\'t play with this deal \nOut of cards')
			continue
	except:
		print('input must be a number(integer)')
	else: break















'''MY SECOND APPROACH(element grabbing)
#NOTE: In the shuffle function above, i use the randrange which grabs the index no of the elements in the list, then i just swap.
In this shuffle function below i used choice and choice grabs the element itself not the index. and elements here are strings. so we cant swap elements in the list since the cant get the index by using the element but we can access the element by using the index. in otherwords we have to count up to the elements using the for loop and using the count value as the index of the element. inorder to catch all IndexError we use the try/except block
def shuffle(lisT):
	try:
		for i in range(len(lisT)):
			for j in lisT:
				indexNo1= indexNo2=0
				ind = choice(lisT[i+1:-2])
				for k in lisT:
					if k == ind:
						break
					indexNo1 += 1
				ind = indexNo1
				for l in lisT:
					if l == j:
						break
					indexNo2 += 1
				j = indexNo2 
				
				lisT[j], lisT[ind] = lisT[ind], lisT[j]
	
		return lisT
	except IndexError:
		return lisT'''	



'''awa's code'
def shuffle(list):
	from random import randrange
	new_list = [ ]
	while(len(list)) > 0:
		rand_no = randrange(len(list))
		shuffle = list.pop(rand_no)
		new_list.append(shuffle)
	return (new_list)'''