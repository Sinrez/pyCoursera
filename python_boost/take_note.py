def take_note(name, str_txt, tags):
    dictionary = dict(name = name, str = str_txt, tags = list(tags))
    return dictionary

all_notes_test = []
def input_notes():
    go_input = 'Y'
    while go_input != 'N':
        note_name = input('Введите название заметки: ')
        note_text = input('Введите текст заметки: ')
        note_tags = input('Введите тэги заметки через запятую: ').split(',')
        go_input = input('Ввести еще одну заметку? Y/N: ').upper()
        all_notes_test.append(take_note(note_name, note_text, note_tags))
input_notes()

def all_notes(tag, notes):
    res = []
    for dict in notes:
        if tag in dict['tags']:
            res.append(dict)
    return ' '.join(map(str, res)).strip('{').strip('}')

def main():
    the_tag = input('Ввведите тэг для поиска заметки или Q для выхода: ')
    if the_tag.upper() == 'Q':
        exit()
    elif all_notes(the_tag,all_notes_test) is None:
        print("Нет заметки по такому тэгу")
    else:
        print(all_notes(the_tag,all_notes_test))

main()


