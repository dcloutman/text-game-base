from typing import TYPE_CHECKING
from src.lib import BaseLandNode

class HillyLandNode (BaseLandNode):

    def __init__ (self, neighbor_north = None, neighbor_east = None, neighbor_south = None, neighbor_west = None):
        super().__init__ (neighbor_north = neighbor_north, neighbor_east = neighbor_east, neighbor_south = neighbor_south, neighbor_west = neighbor_west)
        self.description = "You stand atop a small hill. Tall grass surrounds you. A few trees dot the landscape of rolling hills that extent to the horizon."


