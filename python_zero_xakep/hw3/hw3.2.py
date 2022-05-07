# 2 Напишите программу которая содержит список матерных слов, далее открывает какой-либо файл с текстом,
# заменяет в нем матерные слова на строку "LOL" и записывает результат во второй файл

from rapidfuzz import process, fuzz

def censor():
    badwords = ['fuck', 'fack', 'Fuck', 'Fack', 'FUCK', 'FACK']
    try:
        with open('/content/mat_test', 'r') as badfile, open("censor.txt", "w") as write_file:
            for line in badfile:
                for word in line:
                    s = process.extractOne(word, badwords, scorer=fuzz.WRatio)
                    if s[1] > 50:
                        word = word.replace(word, 'LOL')
                    write_file.write(word)

    except FileExistsError:
        exit('Что-то сломалось с файлом')
    except FileNotFoundError:
        exit('Файл не найден')
    except Exception:
        exit('Что-то сломалось')


if __name__ == '__main__':
    censor()