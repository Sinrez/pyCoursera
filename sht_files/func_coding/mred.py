def myreduce(func, seq):
    result = func(seq[0], seq[1])
    for el in seq[2:]:
        result = func(result, el)

    return result