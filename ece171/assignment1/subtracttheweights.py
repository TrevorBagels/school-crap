

value = 123 #base 10 decimal value

i = value

def big_pow(v):
	for x in range(9):
		l = pow(2, x)
		if l > v:
			return x - 1

binary_table = []

for f in range(10):
	bp = big_pow(i)
	bpv = pow(2, bp)
	print("Biggest power of two that can fit in", i, "is 2 ^", bp, "=", pow(2, bp))
	binary_table.append(bp)
	i2 = i - bpv #diff. when this hits 0, the process should stop.
	print("\t", i, "-", bpv, "=", i2)
	if i2 == 0:
		break
	i = i2

number = []
for x in range(9):
	number.append(0)

for x in binary_table:
	number[int(x)] = 1

number.reverse()
print("".join([str(x) for x in number]))

#for x in binary_table:
#	print(x, "\t", binary_table[x])