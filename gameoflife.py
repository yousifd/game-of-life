class Cell(object):
	def __init__(self):
		self.state = 0
		self.surroundings = []

class Field(object):
	def __init__(self, i, j):
		self.i = i + 2
		self.j = j + 2
		self.cells = [[Cell() for x in range(self.i)] for x in range(self.j)]
		for k in range(i):
			y = k + 1
			for h in range(j):
				x = h + 1
				self.cells[y][x].surroundings.append(self.cells[y-1][x+1])
				self.cells[y][x].surroundings.append(self.cells[y-1][x])
				self.cells[y][x].surroundings.append(self.cells[y-1][x-1])
				self.cells[y][x].surroundings.append(self.cells[y][x+1])
				self.cells[y][x].surroundings.append(self.cells[y][x-1])
				self.cells[y][x].surroundings.append(self.cells[y+1][x+1])
				self.cells[y][x].surroundings.append(self.cells[y+1][x])
				self.cells[y][x].surroundings.append(self.cells[y+1][x-1])

	def liveCells(self):
		count = 0
		for i in range(self.i):
			for j in range(self.j):
				if self.cells[i][j].state == 1:
					count += 1

	def deadCells(self):
		return abs((self.i * self.j) - liveCells)

	def display(self):
		for i in range(self.i - 2):
			y = i + 1
			for j in range(self.j - 2):
				x = j + 1
				if self.cells[y][x].state == 0:
					print('*'),
			print('\n')

def main():
	field = Field(5, 5)
	field.display()

if __name__ == '__main__':
	main()