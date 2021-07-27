def gen_dgt():
    len_lst = check_dgt('Введите длину списка или q для выхода: ')
    res = [get_dgt(dgt) for dgt in range(len_lst)]
    print(f'Результат: {res}')


def get_dgt(d):
    if d % 2 == 0:
        res = 1
    else:
        res = d % 5
    return res


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
    gen_dgt()
