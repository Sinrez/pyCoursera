
def films_check():

    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
             'Леон', 'Богемская рапсодия', 'Город грехов',
             'Мементо', 'Отступники', 'Деревня']

    likes_films = []

    while True:
        inp_film = input('Введите название фильма или q для выхода s - для вывода списка любимых фильмов: ').strip().capitalize()
        if inp_film == 'Q':
            exit('Работа завершена')
        elif inp_film in films:
            likes_films.append(inp_film)
        elif inp_film == 'S':
            break
        else:
            print('Такого фильма нет, поищите еще')

    print(f"Ваш список фильмов: [{', '.join(map(str, likes_films))}]")

if __name__ == '__main__':
    films_check()
