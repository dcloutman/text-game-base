from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BaseLandNode


class BaseActor (ABC):
    """An interactive game object. Possible subclasses can define players or various types of non-player agents.
    """
    def __init__ (self, current_node: "BaseLandNode" = None):
        self.current_node: BaseLandNode = current_node


    def set_current_node(self, current_node: "BaseLandNode"):
        self.current_node = current_node
