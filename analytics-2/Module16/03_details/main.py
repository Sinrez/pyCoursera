shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

def find_detail():
        count = cost = 0
        det = input('Введите название детали в кирилице: ').strip().lower()
        for i in range(len(shop)):
                if det == shop[i][0]:
                        count += 1
                        cost += shop[i][1]

        print(f'\nКол-во деталей - {count}')
        print(f'Общая стоимость - {cost}')


if __name__ == '__main__':
  find_detail()
