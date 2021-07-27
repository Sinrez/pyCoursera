def sum_dgt(dgt):
    summ = 0
    # dgt = str(dgt)
    for d in dgt:
        summ += int(d)
    return summ

def count_dgt(dgt):
    res = []
    for d in dgt:
        res.append(d)
    return len(res)

def main_dgt():
    dgt = check_dgt('Введите число или q для выхода: ')
    summ_dgt = sum_dgt(dgt)
    countt_dgt = count_dgt(dgt)
    delta = summ_dgt - countt_dgt
    print(f'Сумма цифр : {summ_dgt}')
    print(f'Кол-во цифр в числе: {countt_dgt}')
    print(f'Разность суммы и кол-ва цифр: {delta}')

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
  main_dgt()
