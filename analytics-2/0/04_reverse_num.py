def rev_dgt(dgt):
    return dgt[::-1]

def separat_dgt(dgt):
    parts = dgt.split('.')
    res = parts[1] + '.' + parts[0]
    return float(res)

def main_rev():
    dgt1 = check_dgt('Введите первое число или q для выхода: ')
    dgt2 = check_dgt('Введите второе число или q для выхода: ')
    dgt1_bt = separat_dgt(rev_dgt(dgt1))
    dgt2_bt = separat_dgt(rev_dgt(dgt2))
    print()
    print(f'Первое число наоборот: {dgt1_bt}')
    print(f'Второе число наоборот: {dgt2_bt}')
    print(f'Сумма: {dgt1_bt + dgt2_bt}')

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
    main_rev()
