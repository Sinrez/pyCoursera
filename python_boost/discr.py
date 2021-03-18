# дискриминант квадратного уравнения ax 2 + bx + c.
def discr():
    print('Находим дискриминант квадратного уравнения ax 2 + bx + c')
    a = int(input('введите a: '))
    b = int(input('введите b: '))
    c = int(input('введите c: '))
    discriminant = (b ** 2) - (4 * a * c)
    return discriminant
print(discr())
