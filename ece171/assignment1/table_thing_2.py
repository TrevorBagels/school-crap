import math
def to_binary(v, min_bit_count=0):
	b = [] #bits
	if v == 0: return 0
	bit_count = int(math.log2(v)) #word size, also the first time I've ever used log functions for a reason other than math class.
	
	bit_count = max(bit_count, min_bit_count) #adds zero-padding

	for i in range(bit_count + 1): b.append(0) #sets the bits all to 0


	for x in range(bit_count + 1): #using radix division
		q = int(v / 2) #quotient 
		r = ((v / 2) - int(v / 2)) * 2 # 0 or 1 (remainder)
		b[bit_count - x] = int(r) #set the bit to the value of the remainder (in reverse)
		v = q #set the next value that we use to the quotient we just got, and then repeat the process until we run out of bits

	return "".join([str(x) for x in b])

#to octal and to hex are basically the same as to binary, just use 8 and 16 instead of 2
def to_octal(v):
	b = []
	if v == 0: return 0
	word_size = int(math.log(v, 8)) #word size

	for i in range(word_size + 1): b.append(0)


	for x in range(word_size + 1):
		q = int(v / 8)
		r = ((v / 8) - int(v / 8)) * 8 #something between 0-8
		b[word_size - x] = int(r)
		v = q

	return "".join([str(x) for x in b])
def to_hex(v):
	b = []
	if v == 0: return 0
	word_size = int(math.log(v, 16)) #word size

	for i in range(word_size + 1): b.append(0)

	mapping = []
	for x in range(10):
		mapping.append(x)
	for x in range(6):
		mapping.append("ABCDEF"[x])


	for x in range(word_size + 1):
		q = int(v / 16)
		r = ((v / 16) - int(v / 16)) * 16 # 0-16
		b[word_size - x] = mapping[int(r)]
		v = q

	return "".join([str(x) for x in b])


#hex numbers between 0x00 and 0x20 (0 - 2^5)

for i in range(32 + 1):
	print("0x" + str(to_hex(i)), "\t", to_binary(i, min_bit_count=5))