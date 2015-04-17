from pyglet import app
from pyglet import clock
from pyglet import image
from pyglet import sprite
from pyglet import graphics
from pyglet.window import Window
from pyglet.window import key

WIDTH = 360
HEIGHT = 360

# Import Image
onImage = image.load("Yellow.png")
offImage = image.load("Red.png")

class Cell(object):
	def __init__(self, x, y, batch):
		self.state = 0
		self.futureState = 0
		self.x = x
		self.y = y

		self.image = sprite.Sprite(offImage, x=self.x, y=self.y, batch=batch)

		self.surroundings = []

	def getLiving(self):
		living = 0
		for cell in self.surroundings:
			if cell.state == 1:
				living += 1
		return living

	def update(self, batch):
		self.x = self.image.x
		self.y = self.image.y
		if self.state == 1:
			# Set image to on
			# check if you can just change the image for the sprite instead of creating a new one
			self.image.delete()
			self.image = sprite.Sprite(onImage, x=self.x, y=self.y, batch=batch)
		else:
			# Set image to off
			self.image.delete()
			self.image = sprite.Sprite(offImage, x=self.x, y=self.y, batch=batch)
		print("Set State to %i") % self.state

class Field(object):
	def __init__(self, i, j):
		self.batch = graphics.Batch()

		# use this to update the location of each cell
		self.x = 0
		self.y = HEIGHT - 36
		self.i = i + 2
		self.j = j + 2
		self.cells = [[Cell(self.x, self.y, self.batch) for x in range(self.i)] for x in range(self.j)]
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
				self.cells[y][x].image.x = self.x
				self.cells[y][x].image.y = self.y
				self.x += 36
			self.x = 0
			self.y -= 36

	def liveCells(self):
		count = 0
		for i in range(self.i):
			for j in range(self.j):
				if self.cells[i][j].state == 1:
					count += 1
		return count

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

	def update(self, dt):
		for row in self.cells:
			for cell in row:
				if cell.getLiving() == 3:
					cell.futureState = 1
				elif cell.getLiving == 2:
					continue
				else:
					cell.futureState = 0

	    # WTF is this for when you can directly set the state in the previous loop?
		for row in self.cells:
			for cell in row:
				cell.state = cell.futureState
				# Update the visual cells when you change the state
				cell.update(self.batch)

	def reviveCells(self, listOfTupels):
		for t in listOfTupels:
			self.cells[t[1]][t[0]].state = 1
			# Update the cells the moment you set the values
			self.cells[t[1]][t[0]].update(self.batch)

# Set up window and keyboard
window = Window(width=WIDTH, height=HEIGHT)

def main(dt):
	# Get User input for the size
	# Update the width and the Height * 36
	# Ask for the preset values for the blocks

	field = Field(10, 10)
	field.reviveCells([(1,5), (2,5), (3,5), (4,5),(5,5),(6,5),(6,5),(7,5),(8,5),(9,5),(10,5)])

	@window.event
	def on_draw():
		window.clear()
		field.batch.draw()

	@window.event
	def on_key_press(symbol, modifiers):
		if symbol == key.SPACE:
			field.update()

	# clock.schedule_interval(field.update, 0.5)

clock.schedule_once(main, 0)

if __name__ == '__main__':
	# main(0)
	app.run()