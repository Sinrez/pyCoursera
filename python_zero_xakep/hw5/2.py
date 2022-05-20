# 2) Создайте программу,
# которая запускает какую-нибудь стороннюю утилиту командной строки, перехватывает её вывод и сохраняет в файл

def check_q(d):
    if d.lower() == 'q':
        exit(f'Работа завершена')
    elif not d.isdigit():
        exit(f'Нужно ввести число!')

def inp_file(data):
    try:
        with open("res.txt", "wb") as write_file:
            write_file.write(data)
    except FileExistsError:
        exit('Что-то сломалось с файлом')
    except FileNotFoundError:
        exit('Файл не найден')
    except Exception:
        exit('Что-то сломалось')

def crutch_ping(count):
    from subprocess import Popen, PIPE
    import os
    #Любанович в своей книжке импорт пилит прямо внутри функций или классов - понравилось решения, компактно :)

    args = ["ping", "-c", count, "www.ya.ru"]
    process = Popen(args, stdout=PIPE)
    data, error = process.communicate()  # Распаковка кортежа
    if error:
        exit(f'Что-то сломалось с ошибкой: {error}')
    inp_file(data)
    print(f'Произведена запись в файл res.txt, расположенный в {os.path.abspath("res.txt")}')
    print('*' * 25)
    print(data.decode(encoding='cp866'))

def main():
    count = input('Введите кол-во повторов ping: ').strip()
    print('*' * 25)
    check_q(count)
    crutch_ping(count)

if __name__ == '__main__':
    main()
