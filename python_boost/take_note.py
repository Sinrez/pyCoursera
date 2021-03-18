def take_note(name, str_txt, *tags):
    dictionary = dict(name = name, str = str_txt, tags = list(tags))
    return dictionary

# test
print(take_note('test_note_1', 'Тестовя заметка 1','заметка','первая','цели'))

# all_notes = []
# def all_notes(tag, notes):
#     for

