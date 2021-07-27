def count_dgt():
    y1 = int(check_dgt('Введите первый год: '))
    y2 = int(check_dgt('Введите второй год: '))

    if y1 > y2:
        y1, y2 = y2, y1

    print()
    print(f'Года от {y1} до {y2} с тремя одинаковыми цифрами:')
    for y in range(y1, y2 + 1):
        s = str(y)
        if s.count(s[0]) == 3 or s.count(s[1]) == 3 or s.count(s[2]) == 3:
            print(y)


def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isalpha() == True:
            print('Нужно ввести число!')
        else:
            return count_debtor


if __name__ == '__main__':
    count_dgt()
