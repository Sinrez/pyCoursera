import random

# 1. Даны два числа n и m. Создайте матрицу размером n на m и
# заполните ее символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def make_matrix():
    a = []
    try:
        n, m = [int(a) for a in input('Введите 2 числа через пробел, для завершения нажмите Enter: ').split() if not check_dgt(a)]
    except ValueError:
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


# 2. Посчитать в файле количество слов длины 5
"""
Тут возникла идея внтури сделать функцию sep для очистки каждого слова в списке слов из файла от лишних символов,
но с вариантом принимать на вход слово, затем к нему вызывать replace с подстановкой символа для замены из списка разделителей
- не сработало.
"""
def count_words():
    name = input('Введите путь к файлу: ').strip()
    # def sep(w):
    #     separators = [',', '.', '*', '-', ':', '%', '$', '@', '#']
    #     for s in separators:
    #         w.replace(s, '')

    try:
        words_str = open(name, 'r').read()
        words_lst = words_str.split(' ')
        words_lst_pure = []

        for w in words_lst:
            # for s in separators:
                words_lst_pure.append(w.replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('*', '').replace('-', ''))
            # words_lst_pure.append(sep(w))
        words_set = set(words_lst_pure)
        count = 0
        for w in words_set:
            if len(w) == 5:
                count += 1
        print(f'Количество слов длины 5 в файле равно: {count}')
    except FileNotFoundError:
        print('Что-то не так с файлом, проверьте корректность пути, наименование и тд')
    except:
        print('Что-то пошло совсем не так')

# 3. Создать случайную матрицу размера m x n, обнулить все элементы выше главной диагонали, записать ее в файл

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def matrix_gen():
    m = input('Введите кол-во строк матрицы: ').strip()
    n = input('Введите кол-во столбцов матрицы: ').strip()
    check_dgt(m)
    check_dgt(n)
    m = int(m)
    n = int(n)

    Matrix = [[random.randint(1, 11) for j in range(n)] for i in range(m)]
    Matrix_res = [[ Matrix[i][j] for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i < j:
                Matrix_res[i][j] = 0

    return Matrix_res

def matrix_file(matrix):
    try:
        f = open("Res.txt", "w")
        for row in matrix:
            print(*row, file=f)
        f.close()
    except:
        print('Проблемы с записью в файл')

if __name__ == '__main__':
    #1
    # make_matrix()
    #2
    count_words()
    #3
    # matrix_file(matrix_gen())