def take_note(name, str_txt, *tags):
    dictionary = dict(name = name, str = str_txt, tags = list(tags))
    return dictionary

# test
# print(take_note('test_note_1', 'Тестовя заметка 1','заметка','первая','цели'))

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
print(all_notes_test)
# all_notes_test =  [{'name': 'заметка1', 'str': 'раз два три', 'tags': ['зам1', '1зам', '11']},
# {'name': 'заметкО2', 'str': 'тестовая заметка снова', 'tags': ['зам2', '2зам', '2']}]

def all_notes(tag, notes):
    for dict in notes:
        if tag in dict['tags']:
            return dict


print(all_notes('зам1',all_notes_test))


