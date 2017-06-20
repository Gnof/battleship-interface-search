"""
An interface search algorithm utilizing logic
from the Battleship board game.
A user can pick a point at random to start, and
begin systematically looking for the item until it is found.
Subsequent choices following the first point will can be random,
or skewed by a weight of the location likelihood or by properties
of the object being searched for.
"""

class SearchArea(object):
	""" 
	A definition of a square area being searched
	A collection of Search Areas can make up a more
	complex area to search
	"""
	def __init__(self, x, y):
		# Dimensions of the search area 
		self.dimensions = (x,y)
		# The location hash that tracks what has been searched
		self.loc_hash = dict()
		# A set of weights as a search algo starting point
		self.loc_weights = dict()

		