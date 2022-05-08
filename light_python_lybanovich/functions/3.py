# Определите.декоратор.test,.который.выводит.строку.'start'.
# при.вызове.функ- ции.и.строку.'end',.когда.функция.завершает.свою.работу.

def test(func):
    def nfunc(*args, **kwargs):
        print('Старт')
        res = func(*args, **kwargs)
        print('end')
    return nfunc

@test
def priv():
    print('Привет, привет')

priv()