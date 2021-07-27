def video_card():
    count_cards = int(check_dgt('Введите кол-во видеокарт или q для выхода: '))
    cards_list_first = []
    cards_res = []

    for i in range(1, count_cards + 1):
        card = int(check_dgt(f'{i} Видеокарта: '))
        cards_list_first.append(card)

    max_card = max(cards_list_first)
    for i in range(len(cards_list_first)):
        if cards_list_first[i] != max_card:
            cards_res.append(cards_list_first[i])

    print()
    print(f"Старый список видеокарт: [{' '.join(map(str, cards_list_first))}]")
    print(f"Новый список видеокарт: [{' '.join(map(str, cards_res))}]")


def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isdigit() == False:
            print('Нужно ввести число!')
        else:
            return count_debtor


if __name__ == '__main__':
    video_card()
