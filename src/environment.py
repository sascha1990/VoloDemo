from abc import ABC, abstractmethod
from math_util import *
from copy import copy
from logger import *

class Environment(ABC):
    @abstractmethod
    def is_within(self, coord):
        pass

    @abstractmethod
    def _get_intersection(self, coord, velocity):
        pass

    @abstractmethod
    def check_movement(self, agent):
        pass
    

class CuboidEnvironment(Environment):
    def __init__(self, shape) -> None:
        self._shape = shape
    
    def is_within(self, coord):
        for c1, c2 in zip(coord, self._shape):
            if c1 > c2 or c1 < 0:
                return False
        
        return True

    @track_method
    def _get_intersection(self, coord, velocity):
        future_position = vector_add(coord, velocity)

        if self.is_within(coord) and self.is_within(future_position):
            return None

        dir = argmax(vector_abs(velocity))

        intersection = copy(coord)

        if velocity[dir] < 0:
            intersection[dir] = 0
        else:
            intersection[dir] = self._shape[dir]
        
        return intersection
    
    def check_movement(self, agent):
        return self._get_intersection(agent.position, agent.velocity)

if __name__ == '__main__':
    env = CuboidEnvironment([1,1,1])

    print(env._get_intersection([0.5, 0.5, 0.5], [0, 0.5, 0]))
