def path(*arg):
    res = ["",]
    for a in arg:
        res.append(a)
    res = '/'.join(res)
    return res
