

def nod():
    n = int(check_dgt('Введите число: '))
    i = 1
    while i <= n:
        i = i + 1
        if n % i == 0:
            print(f'Наименьший делитель, отличный от единицы: {i}')
            break

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
    nod()
