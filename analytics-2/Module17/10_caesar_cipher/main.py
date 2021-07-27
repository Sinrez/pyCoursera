def cesar():
    msg = input('Введите сообщение: ').strip()
    k = check_dgt('Введите сдвиг или q для выхода: ')
    res_list = [msg[(i - k) % len(msg)] for i in range(len(msg))]
    # тут мощностью алфавита считаю кол-во символов входящей строки
    print(f"Зашифрованное сообщение: {''.join(res_list)}")


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
    cesar()
