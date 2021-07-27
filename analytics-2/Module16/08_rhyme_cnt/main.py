def round_game():
    people_count = check_dgt('Кол-во человек или q для выхода: ')
    dgt = check_dgt('Какое число в считалке? ')
    print(f'Значит, выбывает каждый {dgt} человек')
    dgt_list = list(range(1, people_count + 1))

    for i in range(dgt - len(dgt_list) + 1):
        print(f'\nТекущий круг людей: {dgt_list}')
        print(f'Начало счёта с номера {dgt_list[0]}')
        if dgt > len(dgt_list):
            dgt -= len(dgt_list)
        if abs(dgt) <= len(dgt_list):
            print(f'Выбывает человек под номером {dgt_list[dgt - 1]}')
            del(dgt_list[dgt - 1])
        dgt -= 2

    print(f'\nТекущий круг людей: {dgt_list}')
    if dgt % 2 == 0:
        print(f'Начало счёта с номера {dgt_list[0]}')
        print(f'Выбывает человек под номером {dgt_list[0]}')
        del(dgt_list[0])
    else:
        print(f'Начало счёта с номера {dgt_list[1]}')
        print(f'Выбывает человек под номером {dgt_list[1]}')
        del (dgt_list[1])
    print(f'\nОстался человек под номером {dgt_list[0]}')

def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isdigit() == False:
            print('Нужно ввести число!')
        else:
            return int(count_debtor)

if __name__ == '__main__':
    round_game()
