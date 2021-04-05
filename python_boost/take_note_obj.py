import time
import json

"Реализация Zettelkasten https://habr.com/ru/post/508672/"


class Note():
    "класс заметки"

    def __init__(self):
        self.name = ''
        self.str_txt = ''
        self.tags = []
        self.date_time = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())
        self.__all_notes_test = []
        self.__tmp_notes = []

    def set_dict_param(self, name, str_txt, tags):
        self.name = name
        self.str_txt = str_txt
        self.tags = tags

    def set_all_notes_test(self, all_notes_test):
        self.__all_notes_test.append(all_notes_test)

    def extend_notes_test(self, temp_list):
        self.__all_notes_test.extend(temp_list)

    def get_all_notes_test(self):
        return self.__all_notes_test

    def set_notes_dictionary(self):
        dictionary = dict(name=self.name, str=self.str_txt, tags=self.tags, date_time=self.date_time)
        return dictionary

    def save_note(self, __all_notes_test):
        "сохранение словаря заметок в json-файл в режиме записи"
        with open("notes_obj.txt", "w") as write_file:
            json_string = json.dumps(self.__all_notes_test)
            write_file.write(json_string)

    def return_before_notes(self):
        "выборка ранее сохраненных заметок из файла"
        with open('notes_obj.txt', 'r') as f:
            self.__tmp_notes = list(json.load(f))
        return self.__tmp_notes


class ZettelKasten():
    "Класс обработки заметок"

    def __init__(self, tag):
        self.tag = tag

    def return_all_notes(self):
        "чтение словаря заметок из json-файла"
        with open('notes_obj.txt', 'r') as f:
            text = json.load(f)
            return list(text)

    def all_notes(self, tag, notes):
        "Вывод заметкип оп тэгу из списка в человечном виде"
        res = []
        for dict in notes:
            if tag in dict['tags']:
                res.append(dict)
        return ''.join(map(str, res)).strip('{').strip('}')


def input_notes():
    "пользовательский ввод заметок"
    go_input = 'Y'
    while go_input != 'N':
        note = Note()
        tmp_list_notes = note.return_before_notes()
        note.extend_notes_test(tmp_list_notes)
        note_name = input('Введите название заметки: ')
        note_text = input('Введите текст заметки: ')
        note_tags = input('Введите тэги заметки через пробел: ').split(' ')
        note.set_dict_param(note_name, note_text, note_tags)
        note_dict = note.set_notes_dictionary()
        note.set_all_notes_test(note_dict)
        note.save_note(note_dict)
        go_input = input('Ввести еще одну заметку? Y/N: ').upper()


if __name__ == "__main__":
    "основной блок программы"
    input_notes()
    the_tag = input('Ввведите тэг для поиска заметки, F для вывода всех заметок из файла или Q для выхода: ')
    zettelKasten = ZettelKasten(the_tag)
    list_of_notes = zettelKasten.return_all_notes()
    if the_tag.upper() == 'Q':
        exit('Работа с заметками завершена.')
    elif the_tag.upper() == 'F':
        print(''.join(map(str, list_of_notes)).strip('{').strip('}'))
    elif zettelKasten.all_notes(the_tag, list_of_notes) == '':
        print("Нет заметки по такому тэгу")
    else:
        print(zettelKasten.all_notes(the_tag, list_of_notes))
