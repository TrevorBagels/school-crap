import math

class Main:
	def __init__(self, beq, inputs):
		table_str = ""
		self.input_names = inputs
		self.eq = beq #boolean equation
	
	def generate_truth_table(self):
		#first, start getting combos
		combo_count = int(math.pow(2, len(self.input_names)))
		combos = []
		string_min = "0" * len(self.input_names) #wordsize but it's just zeros
		for x in range(combo_count): #counting in binary... sort of
			_b = bin(x)[2:] #binary value
			b = string_min[:-len(_b)] + _b
			bools = [x == "1" for x in b] #[true, false, true, false, you get the idea]
			result = self.eq(*bools)
			print(" ".join(b), "|", int(result))



def eq(*inputs):
	#H + 'S•W•O
	return inputs[3] or not inputs[2] and inputs[0] and inputs[1]

input_names = ["W", "O", "S", "H"]

'''
In Ecotopia it’s generally illegal to use a car pool lane during weekdays if the car doesn’t 
have at least two occupants.  However, hybrid vehicles can use the lanes any time 
regardless of the number of occupants.  SUVs (even with two or more occupants) are never
allowed to use the car pool lanes (unless they are also hybrids).
Write a Boolean expression in SOP form for 
F(W, O, S, H) which is 1 if the car is 
permitted to use the car pool lane today.  
W is 1 if today is a weekday 
O is 1 if there are two or more occupants
S is 1 if the vehicle is an SUV
H is 1 if the vehicle is a hybrid
'''

m = Main(eq, input_names)
print(" ".join(input_names), "|", "f")
print("-" * (len(" ".join(input_names)) + 4 ) )
m.generate_truth_table()