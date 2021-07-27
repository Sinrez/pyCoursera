def cells():
    count_cells = int(check_dgt('Введите кол-во клеток или q для выхода: '))
    print('Введите эффективности клеток')
    cells_list = []
    res = []

    for i in range(1, count_cells + 1):
        rank = int(check_dgt(f'Эффективность {i} клетки: '))
        cells_list.append(rank)

    for j in range(len(cells_list)):
        if j + 1 > cells_list[j]:
            res.append((cells_list[j]))

    print(f"Неподходящие значения: {' '.join(map(str, res))}")

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
   cells()


