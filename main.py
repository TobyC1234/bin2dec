from math import log2, ceil
from copy import deepcopy

def bintodec(bin): # does stuff
	dec = 0
	for i in range(0, len(bin)):
		dec += int(bin[i]) * 2**i
	return dec

def dectobin(dec): # does other stuff
	if dec == 0:
		return "0"
	bin = ""
	dl = deepcopy(dec)
	for i in range(ceil(log2(dec))+1, -1, -1):
		if dl - 2**i >= 0:
			bin += "1"
			dl -= 2**i
		else:
			bin += "0"
	return bin


for i in range(0, 10):
	#print(f"{str(bin(i))[2:]}: {dectobin(i)}")
	if int(dectobin(i)) == int(str(bin(i))[2:]):
		print(f"{i}: Good")
	else:
		print(f"{i}: Bad")