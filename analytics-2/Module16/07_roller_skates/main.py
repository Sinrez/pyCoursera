legs_size = []
skates_size = []


def list_creator():
    count_skates = check_dgt('Кол-во коньков или q для выхода: ')
    for i in range(count_skates):
        skates_size.append(check_dgt(f'Размер {i + 1} пары: '))

    count_peoples = check_dgt('\nКол-во людей или q для выхода: ')
    for i in range(count_peoples):
        legs_size.append(check_dgt(f'Размер ноги {i + 1} человека: '))

def skates_use():
    count = 0
    list_creator()
    for size_leg in legs_size:
        for i in range(len(skates_size)):
            if skates_size[i] >= size_leg:
                del skates_size[i]
                count += 1
                break
    print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {count}')

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
    skates_use()