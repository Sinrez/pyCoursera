def maps(*x):
    a = x[-1] # беру последний элемент списка  -  это перечень [" python", "SQL", " PHP "]
    F = (list(x[:-1])[::1]) # с первого до предпоследнего в обратном подярке - это f
    L = []
    for i in a:
        for j in F:
            x = j(i)
            i = x
        L.append(i)
    return L