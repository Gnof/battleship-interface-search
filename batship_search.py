from __future__ import division
import logging

logger = logging.getLogger()

class LocationWeight(object):
    """
    The likelihood of an object's location in a searcharea
    An optional parameter in a SearchArea when there is a 
    search bias to increase efficiency
    """
    # TODO: Implement
    def __init__(self, arg):
        
        self.arg = arg


class SearchObject(object):
    """
    The Object being searched for
    """
    def __init__(self, size, props):
        # The size of the object
        # -- a square bounding box around an object rather than 
        # a complex shape

        # size in (x,y)
        self.size = size
        # a generic property dictionary for the object being searched for
        self.props = props

class SearchArea(object):
    """ 
    A definition of a square area being searched
    A collection of Search Areas can make up a more
    complex area to search
    """
    def __init__(self, x, y, loc_hash=dict(), loc_weights=None):
        # Dimensions of the search area 
        self.dimensions = (x,y)
        # The location hash that tracks what has been searched
        self.loc_hash = loc_hash
        # A set of weights as a search algo starting point
        self.loc_weights = loc_weights

        logger.info("New SearchArea (%s,%s) has been created" %(x,y))

    def _inbounds(self,x,y):
        """
        Returns whether the coordinates are within the bounds of the area
        """
        return (x <= self.dimensions[0]) and (y <= self.dimensions[1])

    def _hash_context(self, x,y, so=None):
        """
        Returns the relative proximity to other coordinates already marked in a search area.
        Compares coordinates to contents of location hash, relative size of 
        SearchArea and dimensions of SearchObject and returns a context of the coords to the
        hash
        * - context approaches zero as coordinates approach hash location
        Simple: Larger => further from other coords, Smaller => Closer to other coords
        """
        # iterate through location hash and find distances
        ratio = 0
        so_mod = (0,0)

        # if search object is provided, take into account it's size when outputting context
        if so:
            # x mod => so_mod[0]
            # y mod => so_mod[1]
            so_mod = so.size

        for loc in self.loc_hash:
            curr_x = loc[0]
            curr_y = loc[1]
            # delta of coord and current hash
            delta_x = abs(curr_x - x + so_mod[0])
            delta_y = abs(curr_y - y + so_mod[1])
            # ratio of delta and search area dimension
            ratio_x = delta_x / self.dimensions[0]
            ratio_y = delta_y / self.dimensions[1]
            # overall ratio
            curr_ratio = (ratio_x + ratio_y) / 2
            ratio += curr_ratio

        ratio = ratio / len(self.loc_hash)

        return ratio

    def mark_loc(self, x, y):
        """
        Place the location coordinates into the hash
        """
        # TODO: utilize the hash for the coords
        if (x,y) not in self.loc_hash:
            self.loc_hash[(x,y)] = 0
            logger.info("Coordinates (%s,%s) added to location hash" % (x,y))
        else:
            logger.error("Coordinates (%s,%s) already in location hash, not added" % (x,y))

    def get_loc_context(self,x,y):
        """
        Returns the likelihood of the object being in a location
        given the contents of the location hash of the search area
        and the location weight hash 
        """
        if self._inbounds(x,y):
            # Within the boundaries, check the location weights dictionary if it exists
            # and then the location hash
            context = self._hash_context(x,y)
            logger.info("Context for (%s,%s): %s" % (x,y,context))
            return context
        else:
            logger.error("Coordinates not within bounds of SearchArea: %s, Your Coordinates: (%s,%s)" % (self.dimensions, x, y))
            return 0



        
        