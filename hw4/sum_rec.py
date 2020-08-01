def sum(a, b):
    if b == 0:
        return a
    a += 1
    return sum(a, b - 1)
