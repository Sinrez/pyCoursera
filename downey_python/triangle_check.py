def check_triangle():
    """
    проверка треугольника
    """
    a = int(input('Введите сторону а: '))
    b = int(input('Введите сторону b: '))
    c = int(input('Введите сторону с: '))
    if a <= b + c and c <= a + b and b <= a + c:
        return 'Можно построить треугольник'
    else:
        return 'Нельзя построить треугольник'

if __name__ == "__main__":
    print(check_triangle())