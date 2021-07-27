def sort_list(lst):
    for i in range(len(lst)):
        for curr in range(i, len(lst)):
            if lst[curr] < lst[i]:
                lst[curr], lst[i] = lst[i], lst[curr]


def list_inp():
    size = check_dgt('Введите размер списка или q для выхода: ')
    res = []
    for i in range(size):
        res.append(check_dgt(f'Введите {i + 1} элемент списка: '))
    return res


def main_sort():
    lst = list_inp()
    print(f"\nИзначальный список: [{', '.join(map(str, lst))}]")
    sort_list(lst)
    print(f"\nОтсортированный список: [{', '.join(map(str, lst))}]")


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
    main_sort()
