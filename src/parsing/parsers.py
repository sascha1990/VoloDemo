
'''
This class is used in order to parse input files.
An example input file can be found at VoloDemo/input.txt.

The output of this parser is a dictionary which maps the tokens to the list of parameters.

self._helpers can be updated to process further tokens.
'''
class TxtParser:
    def __init__(self) -> None:
        #helpers keeps methods which are used to parse the different tokens
        self._helpers = {}
        self._helpers['WORLD'] = self._get_env_size
        self._helpers['DRONE'] = self._get_init_pose
        self._helpers['COMMAND'] = self._get_commands
    
    '''
    Processes the input file.

    Parameters
    ----------
    path : str
        The path to the input file
    
    Returns
    ----------
    returns a dictionary which maps the tokens to the list of parameters.
    '''
    def parse_file(self, path):
        f = open(path, "r")
        data = f.read()
        data = self._prune_data(data)

        splits = data.split(';')[1:]#skip head, empty element
        ret = {}
        for split in splits:
            lines = split.split('\n')
            token = lines[0]
            token_parameters = lines[1:]
            arguments = self._clean_up_data(token_parameters)
            
            if token in self._helpers:
                ret[token] = self._helpers[token](arguments)
            else:
                raise ValueError("Unknown Token")
        
        return ret
    
    '''
    Processes the WORLD token.

    Parameters
    ----------
    raw_data : list(str)
        A list of strings. Each string is one line of parameters.

        For the WORLD token, its one line with three numbers.
    
    Returns
    ----------
    returns a list of parameters
    '''
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

    '''
    Processes the DRONE token.

    Parameters
    ----------
    raw_data : list(str)
        A list of strings. Each string is one line of parameters.

        For the DRONE token, its one line with three numbers.
    
    Returns
    ----------
    returns a list of parameters
    '''
    def _get_init_pose(self, raw_data):
        if len(raw_data) != 1:
            raise ValueError("Unknown Format in DRONE")
        
        raw_data = raw_data[0]
        values = raw_data.split(' ')
        
        if(len(values) != 3):
            raise ValueError("Unknown Format in DRONE")
        
        ret = tuple(map(int, values))#immutable
        
        return ret

    '''
    Processes the COMMAND token.

    Parameters
    ----------
    raw_data : list(str)
        A list of strings. Each string is one line of parameters.

        For the COMMAND token, its many lines with three parameters.
    
    Returns
    ----------
    returns a list of parameters
    '''
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
    
    '''
    Checks commands for validity.

    Parameters
    ----------
    commands : list(tuple)
        A list of commands
    '''
    def _check_commands(self, commands):
        for i, command in enumerate(commands):
            num, dir, dist = command
            self._check_command(command)

            if i+1 != num:
                raise ValueError("Missing command after command{}".format(num))

    '''
    Checks one command for validity.

    Parameters
    ----------
    command : tuple
        A single command
    '''
    def _check_command(self, command):
        num, dir, dist = command
        
        if dir not in ['LEFT', 'RIGHT', 'UP', 'DOWN', 'FORWARD', 'BACKWARD']:
            raise ValueError("Invalid direction in command{} ({})".format(num, dir))


    '''
    Cut all the data after EOF
    '''
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
    
    '''
    Filters empty lines from the set of lines.
    '''
    def _clean_up_data(self, data):
        data = [val for val in data if val != '']
        return data
        

if __name__ == '__main__':
    parser = TxtParser()
    parser.parse_file('input.txt')