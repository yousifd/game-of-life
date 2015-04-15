class Cell(object):
	def __init__(self):
		self.state = 0
		self.futureState = 0

		self.surroundings = []

	def getLiving(self):
		living = 0
		for cell in self.surroundings:
			if cell.state == 1:
				living += 1
		return living

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
				if self.cells[y][x].state == 1:
					print('[*]'),
				elif self.cells[y][x].state == 0:
					print('[ ]'),
			print('\n')

	def update(self):
		for row in self.cells:
			for cell in row:
				if cell.getLiving() == 3:
					cell.futureState = 1
				elif cell.getLiving == 2:
					continue
				else:
					cell.futureState = 0

		for row in self.cells:
			for cell in row:
				cell.state = cell.futureState

	def reviveCells(self, listOfTupels):
		for t in listOfTupels:
			self.cells[t[1]][t[0]].state = 1

def main():
	field = Field(10, 10)
	field.reviveCells([(0,5), (2,5), (3,5), (4,5),(5,5),(6,5),(6,5),(7,5),(8,5),(9,5),(10,5)])

	for i in range(5):
		print 'step number: ', i
		field.display()
		field.update()


if __name__ == '__main__':
	main()