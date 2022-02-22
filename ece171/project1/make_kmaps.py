

inp = []

with open("input.txt", "r") as f:
	for x in f.read().strip().split("\n")[1:]:
		a = x.split("|")[0].strip()
		b = x.split("|")[1].strip()
		inp.append((a, b))

grid = []
for x in range(5): grid.append(["x ", "x ", "x ", "x ", "x "])
print(inp)
grid[1][0] = u"A\u0305B\u0305"
grid[2][0] = u"A\u0305B"
grid[3][0] = u"AB"
grid[4][0] = u"AB\u0305"
grid[0][0] = "  "
grid[0][1] = u"C\u0305D\u0305"
grid[0][2] = u"C\u0305D"
grid[0][3] = u"CD"
grid[0][4] = u"CD\u0305"

p = ["00", "01", "11", "10"] #gray code + indexes
for x in inp:
	AB = p.index(x[0][:2]) #Y axis
	CD = p.index(x[0][2:]) #X axis
	grid[AB+1][CD + 1] = x[1] + " "

print("```")
for x in grid:
	print(" ".join(x))
print("```")