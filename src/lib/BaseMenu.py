from typing import List
from abc import ABC

class BaseMenu (ABC):
    def __init__(self, instructions = "", menu_items: List = []) -> None:
        self.menu_items: List = []

    def __str__(self) -> str:
        result: str = ""
        if len(self.instructions) > 0:
            result =  f"{self.inst}\n \n"
        
        for item in self.menu_items:
                result = result + f"{item}\n"
        
        return result.strip()
        