# Подключаем модуль threading для работы с потоками
import threading
# и модуль requests для скачивания файлов из сети
import requests
import shutil
import os

# Функция скачивания файла которую мы будем выполнять
# в новом потоке на входе номер потока и URL скачиваемого файла
def down(nomer, url):
    # Выводим на экран сообщение о старте нового потока
    print(str(nomer)+' поток ('+url+')\n')
    # Получаем имя файла из URL
    (dirname, filename) = os.path.split(url)
    # Запускаем скачивание через GET запрос
    r = requests.get(url, stream=True)
    # Если код ответа сервера 200 (сервер доступен)
    if r.status_code == 200:
        # Открываем файл в режиме побайтовой записи
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            # Созхраняем скачиваемый поток в файл
            shutil.copyfileobj(r.raw, f)
        # Выводим сообщение что поток закончил загрузку
        print(str(nomer) + " поток закончил загрузку\n")
        

# Список URL которые будем скачивать
urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

# Цикл который создаст столько потоков сколько файлов нужно скачать
# Функция enumerate() применяется для так называемых итерируемых объектов
# (список относится к таковым) и создает объект-генератор,
# который генерирует структуры из двух элементов
# – индекса элемента и самого элемента.
for n, url in enumerate(urls):
    # Запускаем поток указав целью функцию down и ее аргументы
    # к nomer прибавляем 1 чтобы номер потока начинался не с нуля
    threading.Thread(target=down, args=[n+1, url]).start()

# Выводим сообщение демонстрирующее что основная программа
# продолжает работать отдельно от созданных потоков
print('\nЕще не завершились потоки а программа уже продолжается\n')



