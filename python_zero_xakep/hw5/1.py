# 1) Создайте программу - скачиватель файлов, которая в одном бесконечном цикле постоянно просит ввести
# url файла который нужно скачать, а в потоках запускает скачивание файлов.

# Подключаем модуль threading для работы с потоками
import threading
# и модуль requests для скачивания файлов из сети
import requests
import shutil
import os
import time

def check_url(in_url):
    """
    Функция отправляет запрос HEAD, чтобы определить, существует ли ресурс, не загружая его содержимое
    """
    try:
        r = requests.head(in_url, allow_redirects=True)
        if r.status_code != 200:
            exit(f'Запрошенный ресурс недоступен, код: {r.status_code}')
    except requests.exceptions.MissingSchema:
        exit('Invalid URL')
    except Exception:
        exit('Ошибка формата запрашиваемого ресурса')

# Функция скачивания файла которую мы будем выполнять
# в новом потоке на входе номер потока и URL скачиваемого файла
def down(nomer, url):
    # Использовал существующую функцию, немного изменил код
    # Выводим на экран сообщение о старте нового потока
    print(str(nomer+1)+' поток ('+url+')\n')
    # Получаем имя файла из URL
    (dirname, filename) = os.path.split(url)
    # Запускаем скачивание через GET запрос
    # тут удалил излишнюю проверку статуса 200 ОК
    r = requests.get(url, stream=True)
    # Открываем файл в режиме побайтовой записи
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
            # Созхраняем скачиваемый поток в файл
        shutil.copyfileobj(r.raw, f)
        # Выводим сообщение что поток закончил загрузку
    print(f'Произведена запись в файл по адресу: {os.path.abspath(filename)}')
    print(str(nomer+1) + " поток закончил загрузку\n")

def main():
    num = 0
    while True:
        in_url = input('Введите адрес файла для скачивания или q для выхода: ').strip()
        if in_url.lower() == 'q':
            exit('Работа завершена!')
        check_url(in_url)
        threading.Thread(target=down, args=[num, in_url]).start()
        num += 1
        time.sleep(2)
        #задержку в 2 подобрал экспериментально: если сделать меньше - получается корявое отображение ввод-вывода
        # возможно на некоторых ресурсах время запроса файла может быть больше и вывод может снова исказиться
        quest = input('Еще скачиваем файл? y/n:\n ').strip()
        if quest.lower() == 'y':
            pass
        else:
            exit('Работа завершена!')

if __name__ == '__main__':
    # для тестов:
    # urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    #         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
    #         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
    #         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    #         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    # https: // www.rulit.me / data / programs / resources / pdf / Stivenson_Python - Sbornik - uprazhneniy_RuLit_Me_677122.pdf

    main()
