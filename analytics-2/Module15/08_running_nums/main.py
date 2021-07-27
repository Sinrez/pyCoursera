def list_offset():
    cont_lst = check_dgt('Введите размер исходного списка или q для выхода: ')
    lst_beg = []

    for i in range(cont_lst):
        lst_beg.append(check_dgt(f'Введите {i + 1} число списка: '))

    offs = check_dgt('Сдвиг: ')
    print(f"Изначальный список: [{', '.join(map(str, lst_beg))}]")
    lst_new = rotate(lst_beg, offs)
    print(f"Сдвинутый список: [{', '.join(map(str, lst_new))}]")


def rotate(l, n):
    return l[-n:] + l[:-n]


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
    list_offset()
