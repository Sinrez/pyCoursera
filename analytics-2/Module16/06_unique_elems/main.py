list1 = []
list2 = []
size1 = 3
size2 = 7


def list_creator(num):
    print(f'Ввод {num} чисел - q для выхода')
    for i in range(num):
        if num == size1:
            list1.append(check_dgt(f'Введите {i + 1} элемент списка: '))
        elif num == size2:
            list2.append(check_dgt(f'Введите {i + 1} элемент списка: '))
        else:
            exit(f'Списка размерности {num} нет')


def list_dgt():
    list_creator(size1)
    list_creator(size2)
    list1.extend(list2)
    print(f'Новый первый список с уникальными элементами: {list(set(list1))}')


def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isalpha() == True:
            print('Нужно ввести число!')
        else:
            return int(count_debtor)


if __name__ == '__main__':
    list_dgt()
