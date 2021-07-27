guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def guests_in():
    name = input(f'Имя гостя: ').strip().capitalize()
    if len(guests) + 1 <= 6:
        guests.append(name)
        print(f'Привет, {name}!')
    else:
        print(f'Прости, {name}, но мест нет.')


def guests_out():
    name = input(f'Имя гостя: ').strip().capitalize()
    try:
        guests.remove(name)
        print(f'Пока, {name}!')
    except ValueError:
        print('Такого гостя нет')


def check_guests():
    print('Для завершения работы введите "Пора спать"')
    while (True):
        print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
        come = input('Гость пришел или ушел? ').strip().lower()
        if come == 'пора спать':
            exit('Вечеринка закончилась, все легли спать.')
        elif come == 'пришел':
            guests_in()
        elif come == 'ушел':
            guests_out()


if __name__ == '__main__':
    check_guests()
