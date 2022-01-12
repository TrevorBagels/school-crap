import math
def to_binary(v, min_bit_count=0):
	b = []
	if v == 0: return 0
	bit_count = int(math.log2(v)) #word size
	
	bit_count = max(bit_count, min_bit_count)

	for i in range(bit_count + 1): b.append(0)


	for x in range(bit_count + 1):
		q = int(v / 2)
		r = ((v / 2) - int(v / 2)) * 2 # 0 or 1
		b[bit_count - x] = int(r)
		v = q


	return "".join([str(x) for x in b])
		
a = []
for x in range(10):
	a.append(x)
for x in range(6):
	a.append("abcdefghi"[x])
for x in range(16):
	print(x, "\t", a[x], "\t", to_binary(x, min_bit_count=3))