import sys

try:
    print(1/0)
except:
    print('Произошла ошибка: ')
    err = sys.exc_info()
    for e in err:
        print(e)
