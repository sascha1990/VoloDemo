from parser import InputParser
from environment import CuboidEnvironment
from agent import DotAgent
from math_util import *


if __name__ == '__main__':
    parser = InputParser()
    config = parser.parse_file('input.txt')

    world_shape = config['WORLD']
    init_position = config['DRONE']
    commands = config['COMMAND']

    print('World Shape:', world_shape)
    print('Init Position:', init_position)

    agent = DotAgent(init_position, 0)
    env = CuboidEnvironment(world_shape)

    for _, dir, dist in commands:
        velocity = dir2vec[dir]
        velocity = vector_scale(velocity, dist)
        
        agent.velocity = velocity

        new_pose = env.check_movement(agent)

        if new_pose is not None:
            print('{}->CRASH IMMINENT - AUTOMATIC COURSE CORRECTION'.format(tuple(agent.velocity)))
            new_velocity = vector_sub(new_pose, agent.position)
            agent.velocity = new_velocity

        agent.apply_velocity()
        

