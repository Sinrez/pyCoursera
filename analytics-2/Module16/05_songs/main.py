violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def get_music():
    times = 0
    count = int(check_dgt('Сколько песен выбрать? Или q для выхода: '))
    for i in range(1, count + 1):
        title = input(f'Название {i} песни: ').strip()
        for j in range(len(violator_songs)):
            if title == violator_songs[j][0]:
                times += violator_songs[j][1]

    print(f'\nОбщее время звучания песен: {times:.2f} минут')

    # print(violator_songs[0][1])

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
    get_music()