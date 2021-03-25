import time
import json
from pprint import pprint
"Реализация Zettelkasten https://habr.com/ru/post/508672/"

all_notes_test = []
tmp_notes=[]

def take_note(name, str_txt, tags):
    "возращаем словарь заметок"
    dt = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())
    dictionary = dict(name = name, str = str_txt, tags = list(tags), date_time = dt)
    return dictionary

def save_note(notes):
    "сохранение словаря заметок в json-файл в режиме дозаписи"
    with open("notes.txt", "w") as write_file:
        json_string = json.dumps(notes)
        write_file.write(json_string)

def input_notes():
    "пользовательский ввод заметок"
    go_input = 'Y'
    while go_input != 'N':
        note_name = input('Введите название заметки: ')
        note_text = input('Введите текст заметки: ')
        note_tags = input('Введите тэги заметки через пробел: ').split(' ')
        go_input = input('Ввести еще одну заметку? Y/N: ').upper()
        all_notes_test.append(take_note(note_name, note_text, note_tags))

def return_before_notes():
    "выборка ранее сохраненных заметок из файла"
    with open('notes.txt', 'r') as f:
        tmp_notes = list(json.load(f))
    return tmp_notes


def return_all_notes():
    "чтение словаря заметок из json-файла"
    with open('notes.txt', 'r') as f:
        text = json.load(f)
        pprint(text)
        # except ValueError:
            # print('Decoding JSON has failed')

def all_notes(tag, notes):
    "Вывод всех заметок из списка в человечном виде"
    res = []
    for dict in notes:
        if tag in dict['tags']:
            res.append(dict)
    return ''.join(map(str, res)).strip('{').strip('}')
    # return ''.join(map(str, res)).strip('{').strip('}').replace('} {', ' || ')

def main():
    "основной блок программы"
    all_notes_test.extend(return_before_notes())
    input_notes()
    save_note(all_notes_test)

    the_tag = input('Ввведите тэг для поиска заметки, F для вывода всех заметок из файла или Q для выхода: ')
    if the_tag.upper() == 'Q':
        exit()
    elif the_tag.upper() == 'F':
        return_all_notes()
    elif all_notes(the_tag,all_notes_test) =='':
        print("Нет заметки по такому тэгу")
    else:
        print(all_notes(the_tag, all_notes_test))

main()


