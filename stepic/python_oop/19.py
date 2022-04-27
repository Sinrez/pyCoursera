class Addition:
    def __call__(self, *args):
        res = 0
        for a in args:
            if isinstance(a, int) or isinstance(a, float):
                res += a
        print(f"Сумма переданных значений = {res}")

add = Addition()

add(10, 20) # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"