from distutils.log import Log
from functools import wraps
import time
import json
from collections import defaultdict

log = defaultdict(list)
filename = 'log.json'

def track_method(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        
        data = {}
        data['input'] = (method_args, method_kwargs)
        data['output'] = method_output
        data['timestamp'] = time.time()
        
        log[method.__name__].append(data)
        
        with open(filename, 'w') as f:
            json.dump(log, f)

        return method_output
    return _impl

def track_output(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        
        data = {}
        data['output'] = method_output
        data['timestamp'] = time.time()
        
        log[method.__name__].append(data)
        
        with open(filename, 'w') as f:
            json.dump(log, f)

        return method_output
    return _impl


if __name__ == '__main__':
    pass