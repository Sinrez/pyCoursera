# Создать матрицу размера m строк на n столбцов вида
# 000000
# 111111
# 222222
# 333333

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def make_matrix_1(m, n):
    Matrix = []
    for i in range(m):
        cols = []
        for j in range(n):
            cols.append(i)
        Matrix.append(cols)
    for row in Matrix:
        print(*row)

# Создать матрицу размера m строк на n столбцов вида
# 100000
# 020000
# 003000
# 000400

def make_matrix_2(m,n):
    Matrix = []
    for i in range(m):
        cols = []
        for j in range(n):
            cols.append(0)
        Matrix.append(cols)

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if i == j:
                Matrix[i][j] = i + 1

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()

# Создать матрицу размера m строк на n столбцов вида
# 1 2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16

def make_matrix_3(m,n):
    Matrix = []

    for i in range(m):
        cols = []
        for j in range(n):
            cols.append(0)
        Matrix.append(cols)

    num = 1
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if i % 2 == 1:
                #движемся начиная с последнего элемента в строке
                Matrix[i][-j - 1] = num
            else:
                Matrix[i][j] = num
            num += 1

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()

# посмотрел второй вар решения:
def make_matrix_3_alt(m,n):
    Matrix = []

    for i in range(m):
        cols = []
        for j in range(n):
            cols.append(0)
        Matrix.append(cols)

    num = 1
    for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                Matrix[i][j] = num
                num += 1

    reverse_matrix = Matrix[1::2]
    # проходим по матрице начиная с первого блочного элемента-строки с шагом 2
    for elem in reverse_matrix:
        elem.reverse()

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()

if __name__ == '__main__':
    m = input('Введите число строк матрицы: ').strip()
    n = input('Введите число столбцов матрицы: ').strip()
    check_dgt(m)
    check_dgt(n)
    m = int(m)
    n = int(n)

    print('-' * 11)
    #задание 1
    print('Задача 1')
    make_matrix_1(m,n)
    print('-' * 11)

    # задание 2
    print('Задача 2')
    make_matrix_2(m,n)
    print('-' * 11)

    # задание 3
    print('Задача 3')
    make_matrix_3(m,n)
    print('-' * 11)

    make_matrix_3_alt(m,n)