from typing import Optional

legend = {
    "1": ".,?!:;",
    "2": "абвг",
    "3": "дежз",
    "4": "ийкл",
    "5": "мноп",
    "6": "рсту",
    "7": "фхцч",
    "8": "шщъы",
    "9": "ьэюя",
    "0": " "
}

def numbers_to_text(numbers: str) -> Optional[str]:
    text = numbers.split()
    for index, word in enumerate(text):
        if len(set(word)) != 1:
            return None
        text[index] = legend[word[0]][len(word) - 1]

    return "".join(text)