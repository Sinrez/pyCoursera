def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')


def input_list() -> list:
    lst = [a for a in input('Введите числа через пробел, для завершения нажмите Enter: ').replace('', ' ').replace(',',
                                                                                                                   ' ').split()
           if
           not check_dgt(a)]
    return lst


# 1. Скачайте с сайта lib.ru любой текстовый документ под именем doc.txt.
# Проверьте кодировку. Напишите программу, которая сделает копию данного файла и сохранит ее в файл doc1.txt
def check_encoding(fl) -> str:
    # добавим возможные популярыные кодировки
    encoding = [
        'utf-8',
        'cp500',
        'utf-16',
        'GBK',
        'windows-1251',
        'ASCII',
        'US-ASCII',
        'Big5'
    ]
    correct_encoding = ''
    for enc in encoding:
        try:
            f = open(fl, encoding=enc).read()
        except (UnicodeDecodeError, LookupError):
            pass
        else:
            correct_encoding = enc
            break
            f.close()
    return correct_encoding


# Посчитайте сколько слов содержит скаченный файл.
def count_fl_wr(fl) -> int:
    try:
        with open(fl, 'rt', encoding=check_encoding(fl)) as f:
            words = [w.strip() for w in f.readlines()]
        print(f'Кол-во слов в файле {len(words)}')
    except (UnicodeDecodeError, LookupError, FileExistsError, FileNotFoundError):
        print('Ошибка работы с файлом')


# 2. В файле input.txt вразнобой записаны целые числа.
# Напишите программу, которая создаст файл output.txt и запишет в него сумму этих чисел.
def sum_from_file(fl):
    try:
        with open(fl, 'rt', encoding=check_encoding(fl)) as f:
            dgts = [int(w.strip()) for w in f.read() if w != ' ']
        sum_d = str(sum(dgts))
    except (UnicodeDecodeError, LookupError, FileExistsError, FileNotFoundError):
        print('Ошибка работы с файлом')
    except ValueError:
        print('Проблемы с типом данных в файле, возможно добавлены не int')
    try:
        with open('output.txt', 'w') as res:
            res.write(sum_d)
    except FileExistsError:
        print('Проблемы с созданием файла с результатом')
    except TypeError:
        print('Проблемы с типом данных, сохраняемых в файл: возможно int, а не str')


# 3. С клавиатуры через пробел вводится список целых чисел.
# Запишите его в файл с именем list1.txt. Затем перенесите из этого файла в файл list2.txt
# все числа, которые стоят на четных местах. Позиции нумеровать с единицы.

def gigits_to_files():
    dgt = input_list()
    try:
        with open('list1.txt', 'w') as res:
            res.write(' '.join(dgt))
    except FileExistsError:
        print('Проблемы с созданием файла с результатом')
    except TypeError:
        print('Проблемы с типом данных, сохраняемых в файл: возможно int, а не str')
    try:
        with open('list1.txt', 'rt') as f:
            dgts = [int(w.strip()) for w in f.read() if w != ' ']
    except (UnicodeDecodeError, LookupError, FileExistsError, FileNotFoundError):
        print('Ошибка работы с файлом')
    except ValueError:
        print('Проблемы со типом данных в файле, возможно добавлены не int')
    try:
        with open('list2.txt', 'w') as res:
            res.write(' '.join(map(str, dgts[::2])))
    except FileExistsError:
        print('Проблемы с созданием файла с результатом')
    except TypeError:
        print('Проблемы с типом данных, сохраняемых в файл: возможно int, а не str')


# 4. Напишите функцию delete_file(f), удаляющую из файла f все символы '+' и '-'.
def delete_file(f):
    try:
        with open(f, "rt") as file:
            file_source = file.read()
    except (UnicodeDecodeError, LookupError, FileExistsError, FileNotFoundError):
        print('Ошибка работы с файлом')
    except ValueError:
        print('Проблемы со типом данных в файле, возможно добавлены не int')
    try:
        with open(f, "wt") as file:
            file.write(file_source.replace("+", "").replace("-", ""))
    except FileExistsError:
        print('Проблемы с созданием файла с результатом')

if __name__ == '__main__':
    # print(f'Кодировка: {check_encoding("/Volumes/D/pyCoursera/skillbrains/doc.txt")}')
    # count_fl_wr('/Volumes/D/pyCoursera/skillbrains/doc.txt')
    # sum_from_file('/Volumes/D/pyCoursera/skillbrains/input.txt')
    # gigits_to_files()
    delete_file('/Volumes/D/pyCoursera/skillbrains/test_plus.txt')
