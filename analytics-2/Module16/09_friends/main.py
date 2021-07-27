def receipt():
    friends_quantity = check_dgt('Кол-во друзей: ')
    debts_quantity = check_dgt('Долговых расписок: ')
    receipts = []

    for friend in range(1, friends_quantity + 1):
        receipts.append(list([friend, 0]))

    for i in range(1, debts_quantity + 1):
        print()
        print(i, 'расписка')
        to_whom = check_dgt('Кому: ')
        from_whom = check_dgt('От кого: ')
        how_much = check_dgt('Сколько: ')
        receipts[to_whom - 1][1] += how_much
        receipts[from_whom - 1][1] -= how_much

    print('\nБаланс друзей: ')
    for x in range(len(receipts)):
        print(receipts[x][0], ':', receipts[x][1])

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
    receipt()
