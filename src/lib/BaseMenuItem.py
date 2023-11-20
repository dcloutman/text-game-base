from abc import ABC

class BaseMenuItem (ABC):
    def __init__(self, shortcut: chr, description:str, action: function) -> None:
        if len(shortcut) != 1:
            raise Exception("Shortcuts must be one character long.")
        
        self.shortcut: chr = shortcut
        self.description: str = description
        self.action: function = action

    def __str__(self) -> str:
        return f"({self.shortcut}) {self.description}"
