from src.util.parser import InputParser
from src.environment.environments import CuboidEnvironment
from src.agent.agents import DotAgent
from src.util.math_util import *
from src.environment.environments import CuboidEnvironment


if __name__ == '__main__':
    parser = InputParser()
    config = parser.parse_file('input.txt')

    world_shape = config['WORLD']
    init_position = config['DRONE']
    commands = config['COMMAND']

    agent = DotAgent(init_position, 0)
    env = CuboidEnvironment(world_shape)

    for _, dir, dist in commands:
        velocity = dir2vec[dir]
        velocity = vector_scale(velocity, dist)
        
        agent.velocity = velocity

        new_pose = env.check_movement(agent)
        updated = agent.update_velocity(new_pose)

        if updated:
            print('{}->CRASH IMMINENT - AUTOMATIC COURSE CORRECTION'.format(tuple(velocity)))

        ret = agent.apply_velocity()

        print('{}->{}'.format(*ret))

        

