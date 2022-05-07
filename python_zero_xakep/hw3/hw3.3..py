# 3 Создайте программу для тестирования, которая хранит в json пары ключ-значение.
# В качестве ключа выступают вопрос с тремя вариантами ответов,
# а в качестве значений - номе правильного ответа.
# Загрузите в программу это json файлов и сделайте чтобы
# она выдавала по очереди эти вопросы и в случае правильного ответа увеличивала
# на единицу значение какой-то переменной, считающей баллы. В конце программа должна выдать результат теста.

import json

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

        try:
            with open("test_quest.json", "r", encoding='UTF-8') as file:
                jsonData = file.read()

        except FileExistsError:
            exit('Что-то сломалось с файлом')
        except FileNotFoundError:
            exit('Файл не найден')
        except Exception:
            exit('Что-то сломалось')

        dict_quest = json.loads(jsonData)

        for quest, answ in dict_quest.items():
            answ_inp = input(quest)
            check_q(answ_inp)
            if answ_inp == dict_quest[quest]:
                total_score += 1
        print('*' * 30)
        print(f'С приземлением! Правильных ответов: {total_score}, набрано баллов: {total_score}')

if __name__ == '__main__':
    test_questions()