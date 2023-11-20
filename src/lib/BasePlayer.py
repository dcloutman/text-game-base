from BaseActor import BaseActor
from abc import ABC

class BasePlayer (BaseActor, ABC):
    def __init__(self) -> None:
        super.__init__()
