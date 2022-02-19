def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')


# 1. Напишите программу, складывающую две матрицы. С клавиатуры вводятся размеры матриц,
# за ними – сами матрицы. Необходимо вывести итоговую матрицу.
# При выводе определяйте для каждого числа 4 позиции и прижимайте его к левой стороне.
# Решение оформить в виде функции.

def input_matrix(n, m) -> list:
    Matrix = []
    for i in range(n):
        cols = []
        for j in range(m):
            d = input(f'Введите {i}{j}-й элемент  матрицы: ')
            check_dgt(d)
            d = int(d)
            cols.append(d)
        Matrix.append(cols)
    return Matrix


def sum_matrix(a, b) -> list:
    result = []
    for i in range(len(a)):
        res = []
        for j in range(len(b)):
            res.append(a[i][j] + b[i][j])
        result.append(res)
    return result


def print_matrix(matrix):
    for m in matrix:
        print(*m)


def work_with_matrix():
    print('По правилам ЛинАла - Складываем только матрицы одной размерности!')
    print()
    try:
        n, m = [int(a) for a in
                input('Введите 2 числа - размерность матриц через пробел, для завершения нажмите Enter: ').split() if
                not check_dgt(a)]
    except (ValueError, UnboundLocalError):
        print('Ошибка ввода:')
    except Exception:
        exit('Случилась системная ошибка')
    print('Введите первую матрицу')
    a = input_matrix(n, m)
    print('Введите вторую матрицу')
    b = input_matrix(n, m)
    print()
    print('Вы ввели превую матрицу:')
    print_matrix(a)
    print()
    print('Вы ввели вторую матрицу:')
    print_matrix(b)
    print()
    print('Вот их сумма:')
    print(sum_matrix(a, b))


# 2. Программа получает на вход размеры матрицы n и m,
# затем n строк по m целых чисел в каждой. Найдите индексы первого вхождения максимального элемента.

def max_elem():
    try:
        n, m = [int(a) for a in input('Введите 2 числа через пробел, для завершения нажмите Enter: ').split() if
                not check_dgt(a)]
    except (ValueError, UnboundLocalError):
        print('Ошибка ввода:')
    except Exception:
        exit('Случилась системная ошибка')
    a = input_matrix(n, m)
    best_i, best_j = 0, 0
    curr_max = a[0][0]
    for i in range(n):
        for j in range(m):
            if a[i][j] > curr_max:
                curr_max = a[i][j]
                best_i, best_j = i, j
    print(f'Индекс максимального элемента {best_i, best_j}')


# 3. Даны два числа n и m. Создайте матрицу размером n на m и заполните ее символами "." и "*"
# в шахматном порядке. В левом верхнем углу должна стоять точка.

def make_matrix():
    a = []
    try:
        n, m = [int(a) for a in input('Введите 2 числа через пробел, для завершения нажмите Enter: ').split() if
                not check_dgt(a)]
    except (ValueError, UnboundLocalError):
        print('Ошибка ввода:')
    except Exception:
        exit('Случилась системная ошибка')

    try:
        for i in range(n):
            a.append([])
            for j in range(m):
                if (i + j) % 2 == 0:
                    a[i].append('.')
                else:
                    a[i].append('*')
        print('-' * n * 2)
        for row in a:
            print(' '.join(row))
    except UnboundLocalError:
        print('Ввели не все числа или больше чем нужно')


if __name__ == '__main__':
    work_with_matrix()
    # make_matrix()
    # max_elem()
