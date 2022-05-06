# 1) Напишите программу, которая просит у пользователя ввода десяти чисел по отдельности,
#             добавляет их в список, а после этого сортирует данный список, и печатает его, умножив каждое число на 10

def check_q(d):
    if d.lower() == 'q':
        exit(f'Работа завершена')
    elif not d.isdigit():
        exit(f'Нужно ввести число!')

def inp_dgt():
    digit_list = []
    print("Нужно ввести 10 числе по отдельности, для выхода - q")
    for i in range(10):
        dgt_in = input(f'Введите {i+1} число: ')
        check_q(dgt_in)
        digit_list.append(int(dgt_in))
    digit_list.sort()
    print('Вы ввели: ')
    print(*digit_list)

if __name__ == '__main__':
    inp_dgt()




