import json

def save_note(notes):
    "сохранение словаря заметок в json-файл в режиме дозаписи"
    with open("notes_test.txt", "a") as write_file:
        json_string = json.dumps(notes)
        write_file.write(json_string)

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

save_note(data)
