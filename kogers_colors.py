#A whole bunch of rgb colors
#Tested to work for opencv

import numpy as np

class Colors():

	def _general_color(self, color, dtype):
		
		if dtype == 'float':
			return [float(i) for i in color]

		elif dtype == 'np.uint8':
			return np.array(
				[color[0], color[1], color[2]], np.uint8)

		else:
			return color

	#BROWNS

	def chocolate_silk(self, dtype='int'):

		color = (49,17,4)
		
		return self._general_color(color, dtype)

	def deep_brown(self, dtype='int'):

		color = (20,8,2)
		
		return self._general_color(color, dtype)

	#BLUES

	def midnight(self, dtype='int'):

		color = (1,15,23)
		
		return self._general_color(color, dtype)

	def blueberry_slate(self, dtype='int'):

		color = (6,56,82)
		
		return self._general_color(color, dtype)


	#TURQOUISE

	def turquoise(self, dtype='int'):
		
		color = (120,192,168)

		return self._general_color(color, dtype)


	def tiffany(self, dtype='int'):
		
		color = (82,183,189)

		return self._general_color(color, dtype)

		82, 183, 189

	#OFF-WHITE

	def bone(self, dtype='int'):
		
		color = (225,235,182)

		return self._general_color(color, dtype)

	#ORANGE

	def orange_gold(self, dtype='int'):
		
		color = (240,168,48)

		return self._general_color(color, dtype)

	def tangerine(self, dtype='int'):
		
		color = (240,129,15)

		return self._general_color(color, dtype)

	#YELLOW

	def sick_yellow(self, dtype='int'):
		
		color = (230,223,68)

		return self._general_color(color, dtype)

	#RED

	def red(self, dtype='int'):
		
		color = (255,0,0)

		return self._general_color(color, dtype)


	#WHITE

	def white(self, dtype='int'):
		
		color = (255,255,255)

		return self._general_color(color, dtype)

	def ivory(self, dtype='int'):
		
		color = (255,255,240)

		return self._general_color(color, dtype)

if __name__ == "__main__":
	c = Colors('int')
	print(c.chocolate_silk())