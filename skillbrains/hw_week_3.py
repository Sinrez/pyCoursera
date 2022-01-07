def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def straight_line(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f'Уравнение прямой: y = {k}x + {b}')

if __name__ == "__main__":
    x1 = input('Введите координатe x1: ')
    y1 = input('Введите координатe y1: ')
    check_dgt(x1)
    check_dgt(y1)
    x1 = int(x1)
    y1 = int(y1)
    x2 = input('Введите координатe x2: ')
    y2 = input('Введите координатe y2: ')
    check_dgt(x2)
    check_dgt(y2)
    x2 = int(x2)
    y2 = int(y2)
    print(5*'-')
    straight_line(x1, y1, x2, y2)