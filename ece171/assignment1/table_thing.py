import math

from colorama.ansi import Fore
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

def print5(a, b, c, d, e):
	print(a, "\t", b, "\t", c, "\t", d, "\t", e)
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

trans = str.maketrans(''.join(superscript_map.keys()), ''.join(superscript_map.values()))

print5("", "Decimal", "Binary", "\tOctal", "Hex")

from colorama import Fore

for x in range(11):
	a, b, c, d, e = "", "", "", "", ""
	a = "2" + str(x).translate(trans)
	b = pow(2, x)
	c = to_binary(b, 11)
	c2 = Fore.CYAN
	i = 0
	i2 = 0
	i3 = 0
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
	for x in c:
		i += 1
		i2 += 1
		c2 += x
		if i == 3:
			i = 0
			c2 += colors[i3]
			i3 += 1
		if i2 == 4:
			i2 = 0
			c2 += " "
	c2 += Fore.WHITE
	"""for x in range(4):
		i = x * 5
		c = c[:i] + " " + c[i:]"""
	d = to_octal(b)
	e = "0x" + to_hex(b)
	print5(a, b, "\t" + str(c2), d, e)