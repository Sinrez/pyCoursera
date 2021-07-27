def sticks():
    sticks_block = list('I' * check_dgt('Кол-во палок или q для выхода: '))
    number_throws = check_dgt('Кол-во бросков: ')

    for i in range(1, number_throws + 1):
        for j in range(check_dgt(f'Бросок {i}. Сбиты палки с номера: ') - 1, check_dgt('по номер: ')):
            sticks_block[j] = '.'
    print(f"Результат: {''.join(sticks_block)}")


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
    sticks()