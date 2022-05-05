import sys

dir2vec = {}
dir2vec['LEFT'] = [-1, 0, 0]
dir2vec['RIGHT'] = [1, 0, 0]

dir2vec['UP'] = [0, 0, 1]
dir2vec['DOWN'] = [0, 0, -1]

dir2vec['FORWARD'] = [0, 1, 0]
dir2vec['BACKWARD'] = [0, -1, 0]

def argmax(vec):
    argmax = None
    maximum = -sys.maxsize - 1

    for i, val in enumerate(vec):
        if val > maximum:
            argmax = i
            maximum = val

    return argmax

def vector_abs(vec):
    return [abs(val) for val in vec]

def vector_add(vec1, vec2):
    return [a+b for a,b in zip(vec1, vec2)]

def vector_sub(vec1, vec2):
    return [a-b for a,b in zip(vec1, vec2)]

def vector_scale(vec, scale):
    return [a*scale for a in vec]
