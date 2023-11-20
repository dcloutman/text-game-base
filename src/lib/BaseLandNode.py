from abc import ABC
from typing import TypeVar
from .BaseActor import BaseActor
from .BaseMenu import BaseMenu

TBaseLandNode = TypeVar("TBaseLandNode", bound="BaseLandNode")

class BaseLandNode (ABC):
    def __init__ (self, neighbor_north = None, neighbor_east = None, neighbor_south = None, neighbor_west = None):
        self.description = ""
        self.inhabitants = set()
        self.menu: BaseMenu = None

        self.neighbor_north = None
        self.neighbor_east = None
        self.neighbor_south = None
        self.neighbor_west = None

        self.connect_neighbor_north(neighbor_north)
        self.connect_neighbor_east(neighbor_east)
        self.connect_neighbor_south(neighbor_south)
        self.connect_neighbor_west(neighbor_west)

    def connect_neighbor_north (self, neighbor_north: TBaseLandNode):
        if neighbor_north == self:
            raise Exception("You cannot connect a land node to itself.")

        if self.neighbor_north == None:
            self.neighbor_north = neighbor_north
            if self.neighbor_north != None:
                self.neighbor_north.neighbor_south = self
        else:
            raise Exception("Cannot overwrite a filled node. Node already has a neighbor to the north.")


    def connect_neighbor_east (self, neighbor_east: TBaseLandNode):
        if neighbor_east == self:
            raise Exception("You cannot connect a land node to itself.")

        if self.neighbor_east == None:
            self.neighbor_east = neighbor_east
            if self.neighbor_east != None:
                self.neighbor_east.neighbor_west = self
        else:
            raise Exception("Cannot overwrite a filled node. Node already has a neighbor to the east.")


    def connect_neighbor_south (self, neighbor_south: TBaseLandNode):
        if neighbor_south == self:
            raise Exception("You cannot connect a land node to itself.")

        if self.neighbor_south == None:
            self.neighbor_south = neighbor_south
            if self.neighbor_south != None:
                self.neighbor_south.neighbor_north = self
        else:
            raise Exception("Cannot overwrite a filled node. Node already has a neighbor to the east.")


    def connect_neighbor_west (self, neighbor_west: TBaseLandNode):
        if neighbor_west == self:
            raise Exception("You cannot connect a land node to itself.")

        if self.neighbor_west == None:
            self.neighbor_west = neighbor_west
            if self.neighbor_west != None:
                self.neighbor_west.neighbor_east = self
        else:
            raise Exception("Cannot overwrite a filled node. Node already has a neighbor to the west.")




    def get_menu(self):
        pass


    def get_menu_string (self):
        return 


    def add_inhabitant (self, inhabitant: BaseActor):
        self.inhabitants.add(BaseActor)

    def remove_inhabitant (self, inhabitant: BaseActor):
        self.inhabitants = self.inhabitants - set(inhabitant)
    
    def print_description(self):
        print(self.description)

    def __str__(self) -> str:
        result = f"{self.description}\n\n"
        if self.menu != None:
            result = f"{result}{str(self.menu)}"
        return result
