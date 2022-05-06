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
        updated = agent.update_target_position(new_pose)

        if updated:
            print('{}->CRASH IMMINENT - AUTOMATIC COURSE CORRECTION'.format(tuple(velocity)))

        
        ret = agent.apply_velocity()

        print('{}->{}'.format(*ret))

        

