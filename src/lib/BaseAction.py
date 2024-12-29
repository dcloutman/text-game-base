from abc import ABC
from .BaseActor import BaseActor

class BaseAction (ABC):
    """Actions are performed by actors on other actors. When an actor acts, it/they emits an action. When an 
    actor is acted upon, it receives an action from the actor initiating the action.
    """
    def __init__(self, initiating_actor: BaseActor) -> None:
        self.initiating_actor: BaseActor = initiating_actor

    def execute_action(self, receiving_actor: BaseActor):
        """This method is executed by the receiving actor when the action is received. It should be customized 
        to the acton type. The receiving_actor parameter allows actions alter the receiving actor based on computed
        outcomes.
        """    
        pass