# 1. Написать функцию, которая получает произвольное число
# параметров целых чисел и возвращает их среднее арифметическое.

def avg_dgt(*args):
    summ = 0
    i = 0
    try:
        for a in args:
            summ += int(a)
            i += 1
        return (f'Среднее арифметическое: {summ / i}')
        # exit()
    except TypeError:
        exit('Нужно ввести число')
    except ValueError:
        exit('Введено не число!')
    except Exception:
        exit('Что-то еще упало')

def run_avg_dgt():
    dgts = input('Введите числа через пробел: ').strip().split()
    if len(dgts) > 1:
        print(avg_dgt(*dgts))
    else:
        print('Нужно ввести более 1 числа.')

# 2. Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться
# конкатенация, т. е. соединение, строк. В остальных случаях введенные числа суммируются.
# Используйте исключения.

def two_val():
    try:
        val_1 = input('Введите первое значение: ').strip()
        val_2 = input('Введите второе значение: ').strip()
        print(float(val_1) + float(val_2))
    except ValueError:
        print(val_1 + val_2)
    except Exception:
        print('Что-то еще упало')

if __name__ == '__main__':
    run_avg_dgt()
    # two_val()

