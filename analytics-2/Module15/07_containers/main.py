def container():
    cont_count = check_dgt('Кол-во контейнеров или q для выхода: ')
    cont_weight = []
    i = 0

    for _ in range(cont_count):
        cont_weight.append(check_dgt('Введите вес контейнера: '))

    new_cont = check_dgt('\nВведите вес нового контейнера: ')

    while i < len(cont_weight) and cont_weight[i] >= new_cont:
        i += 1

    print(f'\nНомер, куда встанет новый контейнер: {i + 1}')


def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isdigit() == False:
            print('Нужно ввести число!')
        elif int(count_debtor) > 200:
            print('Число должно быть не более 200!')
        else:
            return int(count_debtor)


if __name__ == '__main__':
    container()
