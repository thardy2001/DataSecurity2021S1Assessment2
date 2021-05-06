'''
Authors: Tyler Hardy	Lachlan Westfall 
Creation Date: 11/04/21
Purpose: An implementation of DES and experimentation with analysis of its internal features 
'''
import time

left_shift_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

sboxes = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]
expansion_permute =[	
						32, 1, 2, 3, 4, 5,
						 4, 5, 6, 7, 8, 9,
						 8, 9,10,11,12,13,
						12,13,14,15,16,17,
						16,17,18,19,20,21,
						20,21,22,23,24,25,
						24,25,26,27,28,29,
						28,29,30,31,32, 1      ]

inverse_expansion_permute = [2, 3, 4, 5, 8, 9, 10, 11, 14, 15, 16, 17, 20, 21, 22, 23, 26, 27, 28, 29, 32, 33, 34, 35, 38, 39, 40, 41, 44, 45, 46, 47]

compression_permute =[ 	
						14,17,11,24, 1, 5, 3,28,
						15, 6,21,10,23,19,12, 4,
						26, 8,16, 7,27,20,13, 2,
						41,52,31,37,47,55,30,40,
						51,45,33,48,44,49,39,56,
						34,53,46,42,50,36,29,32    ]

straight_permute = [	16, 7,20,21,29,12,28,17,
					 	 1,15,23,26, 5,18,31,10,
						 2, 8,24,14,32,27, 3, 9,
						19,13,30, 6,22,11, 4,25		]
initial_permute = [
						58,50,42,34,26,18,10, 2,
						60,52,44,36,28,20,12, 4,
						62,54,46,38,30,22,14, 6,
						64,56,48,40,32,24,16, 8,
						57,49,41,33,25,17, 9, 1,
						59,51,43,35,27,19,11, 3,
						61,53,45,37,29,21,13, 5,
						63,55,47,39,31,23,15, 7    ]

final_permute = [
						40, 8,48,16,56,24,64,32,
						39, 7,47,15,55,23,63,31,
						38, 6,46,14,54,22,62,30,
						37, 5,45,13,53,21,61,29,
						36, 4,44,12,52,20,60,28,
						35, 3,43,11,51,19,59,27,
						34, 2,42,10,50,18,58,26,
						33, 1,41, 9,49,17,57,25    ]
parity_bit_drop_table =[    
						57,49,41,33,25,17, 9, 1,
					    58,50,42,34,26,18,10, 2,
					    59,51,43,35,27,19,11, 3,
						60,52,44,36,63,55,47,39,
						31,23,15, 7,62,54,46,38,
						30,22,14, 6,61,53,45,37,
						29,21,13, 5,28,20,12, 4    ]


''' UTILITY FUNCTIONS '''

def chunks(lst, n): # Yield successive n-sized chunks from list. FROM: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
	x = []
	for i in range(0, len(lst), n):
		x.append(lst[i:i + n])
	return x 

def IntToBinary(number, bits): # Convert an integer into a binary string with a given bit size
    i = 2**(bits -1)
    result= ""
    while i >= 1: # larger than next biggest power of 2 
        if (number >= i):
            number-= i
            result += "1"      
        else:
            result += "0"
        i = i / 2 
     
    return result

def XOR(x,y):
	result = ""
	for i in range(len(x)):
		if(x[i] == y[i]):
			result+= "0"
		else:
			result+="1"

	return result

def leftShift(number, shifts):
	first_n = number[0:shifts]
	left_shifted = number[shifts:] + first_n
	return left_shifted


def SumArray(x,y):
	new = [None]*len(x)
	for i in range(len(x)):
		new[i] = x[i] + y[i]
	return new

def calculateDifference(p,after):
	temp = XOR(p,after)
	difference = 0
	for i in range(len(p)):
		if(temp[i] == "1"):
			difference+=1
	return difference 

def generateBitVariations(x):
	new_strings = [None]*(len(x) + 1)
	new_strings[0] = x
	for i in range(len(x)):
		if(x[i] == "1"):
			new_strings[i+1] = x[0:i] + "0" + x[i+1:len(x)]
		else:
			new_strings[i+1] = x[0:i] + "1" + x[i+1:len(x)]

	return new_strings

		
''' END UTILITY FUNCTIONS '''
 

''' PERMUTATION FUNCTIONS '''

def compressionPermute(uncompressed):
	compressed= ""
	for i in range(48):
		x = compression_permute[i] - 1
		compressed+= uncompressed[x]

	return compressed 

def expansionPermute(unexpanded):
	expanded = "" 
	for i in range(48):
		x = expansion_permute[i] - 1
		expanded+=unexpanded[x]

	return expanded

def inverseExpansionPermute(original):
	permuted = ""
	for i in range(32):
		permuted+=original[inverse_expansion_permute[i] - 1]

	return permuted

def straightPermute(original):
	permuted = ""
	for i in range(32):
		permuted+=original[straight_permute[i] - 1]


	return permuted

def initialPermute(original):
	permuted = ""
	for i in range(64):
		permuted+=original[initial_permute[i] - 1]


	return permuted

def finalPermute(original):
	permuted = ""
	for i in range(64):
		permuted+=original[final_permute[i] - 1]

	return permuted

def parityDrop(key):
	new_key = ""
	for i in range(56) :
		new_key+= key[parity_bit_drop_table[i] - 1]

	return new_key 

def sBox(value): 
	numbers = chunks(value,6)
	output = ""
	for i in range(len(numbers)):
		row = int((numbers[i][0] + numbers[i][-1]), base = 2)
		column = int(numbers[i][1:-1], base = 2) 
		output+= IntToBinary(sboxes[i][row][column], 4) 

	return output


''' END PERMUTATION FUNCTIONS '''


def DESKeyGenerator(seed_key):
	key = []
	seed_key = parityDrop(seed_key)
	left_half = seed_key[:len(seed_key)//2]
	right_half = seed_key[len(seed_key)//2:]	
	for i in range(16):
		left_half = leftShift(left_half, left_shift_table[i]) 
		right_half = leftShift(right_half, left_shift_table[i])
		key.append(compressionPermute(left_half+right_half))

	return key
    



def FDES0(key, right_text): # Standard DES 
	return straightPermute(sBox(XOR(expansionPermute(right_text),key)))


def FDES1(key, right_text): # Removed XOR with the round key 
	return straightPermute(sBox(expansionPermute(right_text)))


def FDES2(key, right_text): # S-Boxes are replaced with an inverse of the expansion permutation
	return straightPermute(inverseExpansionPermute(XOR(expansionPermute(right_text),key)))


def FDES3(key, right_text): # Removed straight permutation 
	return sBox(XOR(expansionPermute(right_text),key))



def DES(p, k, num_of_rounds, block_size, ver=0, encrypt=True, avalanche=False):
	partial_ciphers = [None]*16
	partial = None
	if(avalanche):
		partial = DES(plaintext,key,num_of_rounds,block_size, ver, True, False)[2]


	round_keys = DESKeyGenerator(k)
	if not encrypt:
		round_keys = round_keys[::-1]

	p = initialPermute(p)
	left = p[:len(p)//2]
	right = p[len(p)//2:]

	round_diff = [None]*16

	# Rounds 
	for i in range(num_of_rounds):
		round_key = round_keys[i]
		temp = right 

		if(ver == 0):
			right = XOR(left,FDES0(round_key, right))
		elif(ver == 1):
			right = XOR(left,FDES1(round_key, right))
		elif(ver == 2):
			right = XOR(left,FDES2(round_key, right))
		else:
			right = XOR(left,FDES3(round_key, right))	

		left = temp
		partial_ciphers[i] = left+right

		if(avalanche):
			
			round_diff[i] = calculateDifference(partial[i],(left+right))
	
	# Final Swap to ensure encrypt = decrypt 
	temp = left
	left = right
	right = temp 
	
	output = finalPermute(left+right)
 	
	return output, round_diff,partial_ciphers



def AvalancheAnalysis(plaintexts,key):

	# With different plaintexts
	sum_difference_variablePlaintext_0 = [0]*16
	sum_difference_variablePlaintext_1 = [0]*16
	sum_difference_variablePlaintext_2 = [0]*16
	sum_difference_variablePlaintext_3 = [0]*16
	for i in range(len(plaintext)):
		difference_by_round = DES(plaintexts[i], key[0], 16,64,0,True,True)[1]
		sum_difference_variablePlaintext_0 = SumArray(difference_by_round,sum_difference_variablePlaintext_0)
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[i], key[0], 16,64,1,True,True)[1]
		sum_difference_variablePlaintext_1 = SumArray(difference_by_round,sum_difference_variablePlaintext_1)	
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[i], key[0], 16,64,2,True,True)[1]
		sum_difference_variablePlaintext_2 = SumArray(difference_by_round,sum_difference_variablePlaintext_2)
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[i], key[0], 16,64,3,True,True)[1]
		sum_difference_variablePlaintext_3 = SumArray(difference_by_round,sum_difference_variablePlaintext_3)
	# Average all of the values 
	 
	for i in range(16):
		sum_difference_variablePlaintext_0[i] = sum_difference_variablePlaintext_0[i]/len(plaintexts)
		sum_difference_variablePlaintext_1[i] = sum_difference_variablePlaintext_1[i]/len(plaintexts)
		sum_difference_variablePlaintext_2[i] = sum_difference_variablePlaintext_2[i]/len(plaintexts)
		sum_difference_variablePlaintext_3[i] = sum_difference_variablePlaintext_3[i]/len(plaintexts)

	# With different Keys 
	sum_difference_variableKey_0 = [0]*16
	sum_difference_variableKey_1 = [0]*16
	sum_difference_variableKey_2 = [0]*16
	sum_difference_variableKey_3 = [0]*16
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[0], key[i], 16,64,0,True,True)[1]
		sum_difference_variableKey_0 = SumArray(difference_by_round,sum_difference_variableKey_0)
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[0], key[i], 16,64,1,True,True)[1]
		sum_difference_variableKey_1 = SumArray(difference_by_round,sum_difference_variableKey_1)	
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[0], key[i], 16,64,2,True,True)[1]
		sum_difference_variableKey_2 = SumArray(difference_by_round,sum_difference_variableKey_2)
	for i in range(len(plaintexts)):
		difference_by_round = DES(plaintexts[0], key[i], 16,64,3,True,True)[1]
		sum_difference_variableKey_3 = SumArray(difference_by_round,sum_difference_variableKey_3)

	for i in range(16):
		sum_difference_variableKey_0[i] = sum_difference_variableKey_0[i]/len(plaintexts)
		sum_difference_variableKey_1[i] = sum_difference_variableKey_1[i]/len(plaintexts)
		sum_difference_variableKey_2[i] = sum_difference_variableKey_2[i]/len(plaintexts)
		sum_difference_variableKey_3[i] = sum_difference_variableKey_3[i]/len(plaintexts)		

	
	print("\n\nP and Pi under K\nRound        DES0    DES1    DES2    DES3")
	for i in range(16):
		print("   ",i,"      ",round(sum_difference_variablePlaintext_0[i],3), "   ",round(sum_difference_variablePlaintext_1[i],3),"   ",round(sum_difference_variablePlaintext_2[i],3),"   ", round(sum_difference_variablePlaintext_3[i],3))
	print("\n\nP under K and Ki\nRound        DES0    DES1    DES2    DES3")
	for i in range(16):
		print("   ",i,"      ",round(sum_difference_variableKey_0[i],3), "   ",round(sum_difference_variableKey_1[i],3),"   ",round(sum_difference_variableKey_2[i],3),"   ", round(sum_difference_variableKey_3[i],3))

	return

start = 0
end = 0

# Read in input file 
file = open("input.txt", "r")
plaintext = file.readline()
key = file.readline()
file.close()
plaintext = plaintext.rstrip("\n")
key = key.rstrip("\n")


text_permutations = generateBitVariations(plaintext)
key_permutations = generateBitVariations(key)


print("ENCRYPTION")
print("Plaintext P:  " +  plaintext)
print("Key K:        " + key)
start = time.perf_counter()
ciphertext = DES(plaintext,key,16,64)[0]
end = time.perf_counter()
print("Ciphertext C: " + ciphertext)
recoveredPlaintext = DES( ciphertext , key,16,64,0,False,False)[0]
print("Recovered P:  " + recoveredPlaintext)

print("Running time: ",end - start, "seconds" )


print("DECRYPTED ? ",plaintext == recoveredPlaintext)

AvalancheAnalysis(text_permutations,key_permutations)






