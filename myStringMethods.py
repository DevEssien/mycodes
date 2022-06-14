
from random import sample

def stringAppend(strParam, elem, index):
	newStr = ''
	for ch in range(len(strParam)):
		if ch != index:
			newStr += strParam[ch]
		elif ch == index:
			newStr += elem + strParam[ch]
	
	return newStr
   # del strParam#delete the initial variable


def strDelete(strParam, ind):
	newStr = ''
	for i in range(len(strParam)):
		if i != ind:
			newStr += strParam[i]
	return newStr
   # del strParam

def strShuffle(strParam):
    shuf = ''.join(sample(strParam, len(strParam)))
    return shuf
