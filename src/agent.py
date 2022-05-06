from abc import ABC, abstractmethod
from math_util import *
from copy import copy
from logger import *

class Agent(ABC):
    def __init__(self, position) -> None:
        super().__init__()
        self.position = position
        self.velocity = [0, 0, 0]
    
    @track_method
    def apply_velocity(self):
        self.position = vector_add(self.position, self.velocity)
        vel = self.velocity
        self.velocity = [0, 0, 0]
        
        print('{}->{}'.format(tuple(vel), tuple(self.position)))

        return tuple(vel), tuple(self.position)

    def update_target_position(self, pos):
        update = pos is not None

        if update:
            new_velocity = vector_sub(pos, self.position)
            self.velocity = new_velocity
        
        return update
        

    
class DotAgent(Agent):
    def __init__(self, position, radius) -> None:
        super().__init__(position)
        self._radius = radius

if __name__ == '__main__':
    pass