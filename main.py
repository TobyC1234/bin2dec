from math import log2, ceil
from copy import deepcopy

def bintodec(bin): # Converts binary to decimal
	dec = 0
	bin = str(bin)
	for i in range(len(bin)): # Iterate over the binary number
		if bin[i] == "1": # If the binary number is a one we want to add the corresponding power of 2
			dec += 2**(len(bin)-i)
	return dec//2 # Have to half it as dec comes out to 2 times the expected value

def dectobin(dec): # Converts decimal to binary
	if dec == 0: # Edge case
		return "0"
	bin = ""
	dl = deepcopy(dec)
	for i in range(ceil(log2(dec))+1, -1, -1): # If we can take away a power of 2 (going highest to lowest)
		if dl - 2**i >= 0:
			bin += "1"
			dl -= 2**i
		else:
			bin += "0"
	return bin
