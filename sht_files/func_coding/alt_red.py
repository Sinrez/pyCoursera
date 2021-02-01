from functools import reduce


def myreduce(func, l):
    return reduce(func, l)