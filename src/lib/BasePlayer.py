from BaseActor import BaseActor
from .BaseLandNode import BaseLandNode
from abc import ABC

class BasePlayer (BaseActor, ABC):
    def __init__(self, current_node: BaseLandNode = None) -> None:
        super.__init__()

    def move(self, direction: chr):
        move_direction = None
        
        match direction:
            case 'N':
                move_direction = self.current_node.neighbor_north
            case 'E':
                move_direction = self.current_node.neighbor_east
            case 'S':
                move_direction = self.current_node.neighbor_south
            case 'W':
                move_direction = self.current_node.neighbor_west

        if move_direction != None:
            self.current_node = move_direction
            
        else:
            print("You can't move that direction.")

