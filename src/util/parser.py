
class InputParser:
    def __init__(self) -> None:
        self._helpers = {}
        self._helpers['WORLD'] = self._get_env_size
        self._helpers['DRONE'] = self._get_init_pose
        self._helpers['COMMAND'] = self._get_commands

    def parse_file(self, path):
        f = open(path, "r")
        data = f.read()
        data = self._prune_data(data)

        splits = data.split(';')[1:]
        ret = {}
        for split in splits:
            lines = split.split('\n')
            meta = lines[0]
            arguments = self._clean_up_data(lines[1:])
            
            if meta in self._helpers:
                ret[meta] = self._helpers[meta](arguments)
            else:
                raise ValueError("Unknown Token")
        
        return ret
    
    def _get_env_size(self, raw_data):
        if len(raw_data) != 1:
            raise ValueError("Unknown Format in WORLD")
        
        raw_data = raw_data[0]
        values = raw_data.split(' ')
        
        if(len(values) != 3):
            raise ValueError("Unknown Format in WORLD")
        
        ret = tuple(map(int, values))#immutable

        for v in ret:
            if v < 0: raise ValueError("Dimensions of the environment must be unsigned")
        
        return ret

    def _get_init_pose(self, raw_data):
        if len(raw_data) != 1:
            raise ValueError("Unknown Format in DRONE")
        
        raw_data = raw_data[0]
        values = raw_data.split(' ')
        
        if(len(values) != 3):
            raise ValueError("Unknown Format in DRONE")
        
        ret = tuple(map(int, values))#immutable
        
        return ret

    def _get_commands(self, raw_data):
        commands = []
        for line in raw_data:
            components = line.split(' ')
            
            if(len(components) != 3):
                raise ValueError("Each COMMAND must have 3 components")
            
            num, dir, dist = components
            command = (int(num), dir.upper(), int(dist))
            commands.append(command)
        
        commands.sort(key=lambda x: x[0])
        commands = tuple(commands) #immutable

        self._check_commands(commands)

        return commands
    
    def _check_commands(self, commands):
        for i, command in enumerate(commands):
            num, dir, dist = command
            self._check_command(command)

            if i+1 != num:
                raise ValueError("Missing command after command{}".format(num))

    def _check_command(self, command):
        num, dir, dist = command
        
        if dir not in ['LEFT', 'RIGHT', 'UP', 'DOWN', 'FORWARD', 'BACKWARD']:
            raise ValueError("Invalid direction in command{} ({})".format(num, dir))


    
    def _prune_data(self, raw_data):
        data = ''
        for line in raw_data.split('\n'):
            if line == 'EOF':
                break
            else:
                data += line + '\n'
        else:
            raise ValueError("EOF not found")
        
        return data
    
    def _clean_up_data(self, data):
        data = [val for val in data if val != '']
        return data
        

if __name__ == '__main__':
    parser = InputParser()
    parser.parse_file('input.txt')