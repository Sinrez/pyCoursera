


class InputError(Exception):
    """Вызывается, когда на сайте-источнике курса не загружены курсы
    при попытке записи пустого значения курса"""
    pass

x = input("Ведите положительное целое число: ")
try:
    x = int(x)

except ValueError as ve:
    raise InputError(f'!!! x = input({x}) {ve}', '-> Допустимы только положительные числа. ')
except InputError as e:
    exit(e.args[0])
    # print(e.args[1])
else:
    print(x)