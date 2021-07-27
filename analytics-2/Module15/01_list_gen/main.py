
def list_gen():
    res = []
    dgt = int(check_dgt('Введите число или q для выхода: '))
    for i in range(dgt + 1):
        if i % 2 == 0:
            res.append(i)
    print(f'Список четных чисел: {res}')

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
  list_gen()

