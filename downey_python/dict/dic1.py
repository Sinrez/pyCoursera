
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

d = {'п': 2, 'о': 1, 'у': 1, 'г': 1, 'а': 1, 'й': 1}

print(invert_dict(d))