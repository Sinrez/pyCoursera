# 2) Создайте программу,
# которая запускает какую-нибудь стороннюю утилиту командной строки, перехватывает её вывод и сохраняет в файл
from subprocess import Popen, PIPE
import os
import validators

def check_is_digit(d):
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

def crutch_ping(count, url_to_ping):
    args = ["ping", "-c", count, url_to_ping]
    process = Popen(args, stdout=PIPE)
    data, error = process.communicate()  # Распаковка кортежа
    if error:
        exit(f'Что-то сломалось с ошибкой: {error}')
    inp_file(data)
    print(f'Произведена запись в файл res.txt, расположенный в {os.path.abspath("res.txt")}')
    print('*' * 25)
    print(data.decode(encoding='cp866'))

def check_url(url_ping):
    if 'http' not in url_ping[:5]:
        url_ping = 'http://'+ url_ping
    elif 'https' not in url_ping[:5]:
        url_ping = 'https://' + url_ping
    # elif 'http://www.' not in url_ping:
    #     url_ping = 'http://www.' + url_ping
    # elif 'https//www.' not in url_ping:
    #     url_ping = 'https//www.' + url_ping
    if not validators.url(url_ping):
        exit('Введен некорректный адрес web-ресурса, повторите попытку!')

def main():
    url_ping = input('Введите адрес ресурса для ping:  ').strip()
    check_url(url_ping)
    count = input('Введите кол-во повторов ping: ').strip()
    print('*' * 25)
    check_is_digit(count)
    crutch_ping(count,url_ping)

if __name__ == '__main__':
    main()
