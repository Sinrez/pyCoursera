# - Составьте программу, которая проведёт несложный тест,
# задавая пользователю 5 разных вопросов, получая от него номера вариантов ответов и считая баллы за правильные ответы.
# В конце программа должна напечатать на сколько вопросов человек ответил правильно.

def check_q(d, total_score=None):
    if d.lower() == 'q':
        exit(f'Работа с тестом завершена, ваш результат: {total_score}')
    elif d not in ('1','2','3'):
        exit(f'Нужно ввести значение варианта ответа 1 или 2 или 3. Работа с тестом завершена, ваш результат: {total_score}')

def test_questions():
        total_score = 0
        print('Пристегните скафандр, введите номер ответа, для выхода введите q')
        print(20 * '*')
        print('Поехали!')
        quest1 = input('Вопрос 1: Кто вывел формулу реактивного движения? 1 - Циолковский, 2 - Браун, 3 - Виннер: ')
        check_q(quest1, total_score)
        if quest1 == '1':
            total_score += 1
        print(20 * '*')
        quest2 = input('Вопрос 2: В каком году А.Ю. Гагарин соверщил первый орбитальный полет? 1 - 1962, 2 - 1961, 3 - 1960: ')
        check_q(quest2, total_score)
        if quest2 == '2':
            total_score += 1
        print(20 * '*')
        quest3 = input(
            'Вопрос 3: Как назвался первый в мире космический аппарат, поднявший на своём борту человека на околоземную орбиту?'
             '1 - Восток, 2 - Восток-1, 3 - Заря: ')
        check_q(quest3, total_score)
        if quest3 == '1':
            total_score += 1
        print(20 * '*')
        quest4 = input(
            'Вопрос 4: В каком году выведе на орбиту первый спутник? 1 - 1962, 2 - 1961, 3 - 1957: ')
        check_q(quest4, total_score)
        if quest4 == '3':
            total_score += 1
        print(20 * '*')
        quest5 = input(
            'Вопрос 5: Какое первое животное выведено на орбиту Земли? 1 - Обезьяна, 2 - Собака, 3 - Кошка: ')
        check_q(quest5, total_score)
        if quest5 == '2':
            total_score += 1
        print(20 * '*')
        print(f'С приземлением! Правильных ответов: {total_score}, набрано баллов: {total_score}')

if __name__ == '__main__':
    test_questions()

