from src.lib.BaseLandNode import BaseLandNode

class PlainLandNode (BaseLandNode):

    def __init__ (self, neighbor_north = None, neighbor_east = None, neighbor_south = None, neighbor_west = None):
        super().__init__ (neighbor_north = neighbor_north, neighbor_east = neighbor_east, neighbor_south = neighbor_south, neighbor_west = neighbor_west)
        self.description = "You are standing in a plain. Tall grass surrounds you. The horizon is flat. No hills or mountains are visible in the distance."


