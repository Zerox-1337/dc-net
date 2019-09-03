"""
Simple implementation that can be used for a 16 bit anonymous DC-protocol.
"""

import numpy as np
import scipy as sp
import time



def xor(x, y):
	result = "";
	for i in range (0, len(x)):
		if (x[i] == y[i]):
			result += "0";
		else:
			result += "1";
	return result;
def invXor(x, y):
	result = "";
	for i in range (0, len(x)):
		if (x[i] == y[i]):
			result += "1";
		else:
			result += "0";
	return result;

def toHex(x):
	return "%X" % int(x, 2);
	#return x.encode('hex_codec')

#My own conversion to binary. 
def toBinary(x):
	result = ""
	for i in range (0, len(x)):
		if (x[i].lower() == "f"):
			result += "1111";
		elif (x[i].lower() == "e"):
			result += "1110";
		elif (x[i].lower() == "d"):
			result += "1101";
		elif (x[i].lower() == "c"):
			result += "1100";
		elif (x[i].lower() == "b"):
			result += "1011";
		elif (x[i].lower() == "a"):
			result += "1010";
		elif (x[i].lower() == "9"):
			result += "1001";
		elif (x[i].lower() == "8"):
			result += "1000";
		elif (x[i].lower() == "7"):
			result += "0111";
		elif (x[i].lower() == "6"):
			result += "0110";
		elif (x[i].lower() == "5"):
			result += "0101";
		elif (x[i].lower() == "4"):
			result += "0100";
		elif (x[i].lower() == "3"):
			result += "0011";
		elif (x[i].lower() == "2"):
			result += "0010";
		elif (x[i].lower() == "1"):
			result += "0001";
		elif (x[i].lower() == "0"):
			result += "0000";
	return result;	

"""

SA = Your shared 16-bit secret with alice
SB = Your shared secret with bob. 
DA = The broadcasted data sent by Alice.
DB = The broadcasted data sent by bob.
M = 16 bit message that you wish to send anonymously. 
b = 1 means you wish to send the message. 0 = you do not want to send the message.

Output = the broadcasted data if b = 0 and the broadcasted data + anonymous message (0000 if no anonymous message was sent)

"""

def DC(SA, SB, DA, DB, M, b):
	if (b == 1):
		result = toHex(xor(xor(toBinary(SA), toBinary(SB)), toBinary(M)))
		return result.zfill(4);
			
	else:
		result1 = xor(toBinary(SA), toBinary(SB));
		result2 = xor(toBinary(DA), toBinary(DB))
		return toHex(result1).zfill(4) + (toHex(xor(result1, result2)).zfill(4));
"""
test vectors 
SA = "27C2"
SB = "0879"
DA = "35F6"
DB = "1A4D"
M = "27BC"
b = 1

"""

SA = "4303"
SB = "1119"
DA = "5137"
DB = "032D"
M = "B571"
b = 1



print (DC(SA, SB, DA, DB, M, b));

