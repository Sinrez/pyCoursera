def count_letters():
    word = input('Введите слово или q для выхода: ').strip().lower()
    conut_let = 0

    if word == 'q':
        exit('Работа завершена')
    else:
        for w in word:
            if word.count(w) < 2:
                conut_let += 1

    print(f'\nКол-во уникальных букв: {conut_let}')


if __name__ == '__main__':
    count_letters()
