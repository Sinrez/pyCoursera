def usm(*args):
    # Начальный аргумент.
    value = args[0]

    # Перебираем все аргументы начиная с первого.
    for arg in args[1:]:
        if type(value) is str:
            value += str(arg)
        else:
            value += int(arg)

    return value