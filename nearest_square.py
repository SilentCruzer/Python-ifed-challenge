import math

def nearest_square(number):
	try:
		nearest = math.floor(math.sqrt(number))
		return nearest*nearest
	except ValueError:
		return 0

