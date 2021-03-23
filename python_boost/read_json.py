import json
from pprint import pprint

# def return_all_notes():
#     # чтение словаря заметок из json-файла
#     with open("data_file.json", "r") as read_file:
#         data = json.load(read_file)
#     return data
#with open('notes.txt', 'r', encoding='utf-8') as f:
# print(return_all_notes())

with open('notes.txt', 'r') as f:
    try:
        text = json.load(f)
        pprint(text)
    except ValueError:
        print('Decoding JSON has failed')


