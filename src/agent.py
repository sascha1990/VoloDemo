from abc import ABC, abstractmethod
from math_util import *
from copy import copy

class Agent(ABC):
    def __init__(self, position) -> None:
        super().__init__()
        self.position = position
        self.velocity = [0, 0, 0]
    
    def apply_velocity(self):
        self.position = vector_add(self.position, self.velocity)
        vel = self.velocity
        self.velocity = [0, 0, 0]
        
        print('{}->{}'.format(tuple(vel), tuple(self.position)))
        

    
class DotAgent(Agent):
    def __init__(self, position, radius) -> None:
        super().__init__(position)
        self._radius = radius

if __name__ == '__main__':
    pass