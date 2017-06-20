import logging

logger = logging.getLogger()

class SearchObject(object):
	"""
	The Object being searched for
	"""
	def __init__(self, size, props):
		# The size of the object
		self.size = size
		# a generic property dictionary for the object being searched for
		self.props = props

class SearchArea(object):
	""" 
	A definition of a square area being searched
	A collection of Search Areas can make up a more
	complex area to search
	"""
	def __init__(self, x, y, loc_hash=dict(), loc_weights=dict()):
		# Dimensions of the search area 
		self.dimensions = (x,y)
		# The location hash that tracks what has been searched
		self.loc_hash = loc_hash
		# A set of weights as a search algo starting point
		self.loc_weights = loc_weights

	def _inbounds(self,x,y):
		"""
		Returns whether the coordinates are within the bounds of the area
		"""
		return (x <= self.dimensions[0]) and (y <= self.dimensions[1])

	def get_loc_context(self,x,y):
		"""
		Returns the likelihood of the object being in a location
		given the contents of the location hash of the search area
		and the location weight hash 
		"""
		if self._inbounds(x,y):
			# Within the boundaries, check the location weights dictionary
			# and then the location hash
			return
		else:
			logger.error("Coordinates not within bounds of SearchArea: %s, Your Coordinates: (%s,%s)" % (self.dimensions, x, y))
			return 0



		
		