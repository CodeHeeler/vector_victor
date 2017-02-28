class ShapeError(Exception):
    pass


def shape(thing):
    n = len(thing)
    #if type(thing[0]) == list:
    #    k = len(thing[0])
    #    return (n,k)
    #else:
    return (n,)


def vector_add(v1, v2):
    if shape(v1) == shape(v2):
        return [a + b for a, b in zip(v1, v2)]
    else:
        raise ShapeError("Cannot add vectors of differing length")


def vector_sub(v1, v2):
    if shape(v1) == shape(v2):
        return [a - b for a, b in zip(v1, v2)]
    else:
        raise ShapeError("Cannot subtract vectors of differing length")


def vector_sum(*args):
    comparisons = [len(arg) == len(args[0]) for arg in args]
    if sum(comparisons) == len(comparisons):
        return [sum(stuff) for stuff in zip(*args)]
    else:
        raise ShapeError("Cannot sum vectors of differing length")


def dot(v1, v2):
    if shape(v1) == shape(v2):
        return sum([a * b for a, b in zip(v1, v2)])
    else:
        raise ShapeError("Cannot dot vectors of differing length")


def vector_multiply(v, num):
    return [a * num for a in v]


def vector_mean():
    pass


def magnitude():
    pass
