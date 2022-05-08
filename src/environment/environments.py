from abc import ABC, abstractmethod
from src.util.math_util import *
from copy import copy
from src.util.logger import *

'''
    Interface for all environments.
    Environment classes contain all the information within the environment.
    This might be obstacles or environment borders.
'''
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
    

'''
    This is an example implementation of an cuboid environment. 
    Thus agents could only move within its borders.
'''
class CuboidEnvironment(Environment):
    def __init__(self, shape) -> None:
        self._shape = shape
    
    def is_within(self, coord):
        for c1, c2 in zip(coord, self._shape):
            if c1 > c2 or c1 < 0:
                return False
        
        return True

    '''
    Returns the closest point, if a collision would happen.
    Returns None if no collision would happen.

    Parameters
    ----------
    coord : list
        A 3D vector as a list with three elements. This is the current position of an agent.
    velocity : list
        A 3D vector as a list with three elements. This is his planned velocity.
    
    Returns
    ----------
    returns None, if no intersection was found. returns the position of the detected collision else.
    '''
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
    
    '''
    Checks a planned movement of an agent.
    Currently only checks for intersections with the borders of the envronment.

    Taking obstacles into account will change this method.
    '''
    def check_movement(self, agent):
        return self._get_intersection(agent.position, agent.velocity)

if __name__ == '__main__':
    env = CuboidEnvironment([1,1,1])

    print(env._get_intersection([0.5, 0.5, 0.5], [0, 0.5, 0]))
