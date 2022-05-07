# 1 Создайте программу которая позволяет вести дневник,
# открывая файл в режиме дозаписи строк в конец файла ('a')
# и записывает полученную от юзера информацию.
# Подумайте как разделить записи в файле несколькими переносами, или линией из подчёркиваний.

import time

def input_notes():
  "ввод заметок"
  go_input = 'Y'
  while go_input != 'N':
    note_name = input('Введите название заметки дневника: ')
    note_text = input('Введите текст заметки: ')
    go_input = input('Ввести еще одну заметку? Y/N: ').upper()
    dt = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())
    try:
        with open("notes.txt", "a") as write_file:
            write_file.write('#' * 40 + '\n')
            write_file.write('Время заметки' + ' ' + dt + '\n')
            write_file.write(note_name + '\n')
            write_file.write(note_text + '\n')
            write_file.write('#' * 40 + '\n')
    except FileExistsError:
        exit('Что-то сломалось с файлом')
    except FileNotFoundError:
        exit('Файл не найден')
    except Exception:
        exit('Что-то сломалось')

def return_all_notes():
    "чтение словаря заметок файла"
    try:
        print('*' * 40)
        print('Вот ваш дневник: ')
        print('*' * 40 + '\n')
        with open('notes.txt', 'r') as f:
          text_in_file = f.read()
          print(text_in_file)
    except FileExistsError:
        exit('Что-то сломалось с файлом')
    except FileNotFoundError:
        exit('Файл не найден')
    except Exception:
        exit('Что-то сломалось')

def main():
    "основной блок программы"
    the_tag = input('Вы работаете с топорной программой ввода заметок, если решили выйти - введите Q, если нет - любую клавишу :) ')
    if the_tag.upper() == 'Q':
      exit('Работа завершена, всего доброго!')
    else:
        input_notes()
        print('')
        return_all_notes()

if __name__ == '__main__':
  main()