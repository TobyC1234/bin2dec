from math import log2, ceil
from copy import deepcopy

def bintodec(bin): # does stuff
	dec = 0
	bin = str(bin)
	for i in range(len(bin)): # Iterate over the binary number
		if bin[i] == "1": # If the binary number is a one we want to add the corresponding power of 2
			dec += 2**(len(bin)-i)
	return dec//2 # Have to half it as dec comes out to 2 times the expected value

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


for i in range(0, 100):
	print(f"{i}: {bintodec(str(bin(i))[2:])}")
__import__('sys').exit()
for i in range(0, 10):
	#print(f"{str(bin(i))[2:]}: {dectobin(i)}")
	if int(dectobin(i)) == int(str(bin(i))[2:]):
		print(f"{i}: Good")
	else:
		print(f"{i}: Bad")