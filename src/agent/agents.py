from abc import ABC, abstractmethod
from src.util.math_util import *
from copy import copy
from src.util.logger import *

'''
    A class used to represent an Agent.
    Agents might have different shapes and behaviours.
'''
class Agent(ABC):
    def __init__(self, position) -> None:
        super().__init__()
        self.position = position
        self.velocity = [0, 0, 0]
    
    '''
    Adds the velocity vector (global) to the current position (global)

    Returns
    ----------
    returns a tuple with the applied velocity and the new position
    '''
    @track_method
    def apply_velocity(self):
        self.position = vector_add(self.position, self.velocity)
        vel = self.velocity
        self.velocity = [0, 0, 0]
        
        return tuple(vel), tuple(self.position)

    '''
    Updates the velocity by taking the closest collision-free position into account.

    Parameters
    ----------
    pos : list
        A 3D vector as a list with three elements. 
    
    Returns
    ----------
    returns a boolean which describes if the velocity was updated or not
    '''
    def update_velocity(self, pos):
        update = pos is not None

        if update:
            new_velocity = vector_sub(pos, self.position)
            self.velocity = new_velocity
        
        return update
        

    
class DotAgent(Agent):
    def __init__(self, position) -> None:
        super().__init__(position)

if __name__ == '__main__':
    pass