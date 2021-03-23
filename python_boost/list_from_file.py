import json

tmp_notes = []

def return_before_notes():
    "выборка ранее сохраненных заметок из файла"
    with open('notes.txt', 'r') as f:
        tmp_notes = list(json.load(f))
    return tmp_notes


print(type(return_before_notes()))