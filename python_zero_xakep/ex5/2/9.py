# Скрипт, который по голосовой команде "напиши что-то"
# пишет сказанный текст в любом поле ввода, в любой программе

#!/usr/bin/env python3
# Установите модуль для распознавания русско речи
# pip install vosk
from vosk import Model, KaldiRecognizer
'''Установите модуль для записи с микрофона
pip install pyaudio
Для Windows возможно понадобится скачать и установить скомпилированную .whl версию
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
(выбрав файл под вашу версию Python и разрядность ОС)
Скачав файл наберите в командной строке pip install путь к скачанному файлу'''
import pyaudio
# Модуль для работы с файловой системой
import os
from os import path
# Подключим модуль для работы с буфером обмена
# (В Linux если нет pip3, apt-get install python3-pip)
# В командной строке или терминале pip install pyperclip
# Для Linux pip3 install pyperclip
import pyperclip
# Модуль для работы с клавиатурой
import keyboard
# Модкль для создания пауз в работе программы
import time
# Модуль для работы с json
import json
# Модуль для открытия браузера
import webbrowser
# Модуль для сравнения строк
from rapidfuzz import process, fuzz

# Ключевые слова фразу после которых нужно напечатать
flags = ['напиши','напечатаю','напечатает','напечатайте','напечатать', 'напечатай', 'введи текст', 'ввести текст']
# Ключевые слова фразу после которых нужно найти в сети
flags2 = ['найти', 'найди', 'поиск', 'поищи', 'искать']
# Ключевые слова для открытия файлов с рабочего стола и папки Документы
flags3 = ['открой', 'открыть', 'запусти', 'запустить']
# папки в которых будет проходить поиск файлов по имени
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
mydirs = [desktop]
# загружаем модель распознавания речи
# папка model должна быть рядом со скриптом
model = Model("model")
# Объявляем распознаватель речи и его частоту дискретизации звука
rec = KaldiRecognizer(model, 16000)

# Слушаем звук с микрофона
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Функция ищет есть ли в сказанной фразе ключевые слова из списка flags
def isflag(txt, xflags):
    # Проходим по списку ключевых слов
    for flagword in xflags:
        # Если ключевое слово есть во фразе
        if flagword in txt:
            # Возвращаем это слово
            return flagword

# Функция получает словарь всех файлов в списке папок mydirs
def getfilelist(mydirs):
    myfiles = {}
    for mydir in mydirs:
        for root, dirs, files in os.walk(mydir):
            for name in files:
                # это полный путь к файлу
                fullname = os.path.join(root, name)
                myfiles[name]  = fullname
                # это имя файла без полного пути и без расширения
                fname, _ = path.splitext(name)
    # Возвращаем словарь в котором ключи - имена файлов а значения - пути к ним
    return myfiles

# Функция которая будет открывать файл
def openfile(txt):
    # Получим список всех файлов в тех папках где надо искать
    mylist = getfilelist(mydirs)
    # Найдем имя файла наиболее похожее на сказанное
    s = process.extractOne(txt, mylist.keys(), scorer = fuzz.ratio)[0]
    # Получим полный путь к файлу по его имени из нашего словаря
    file = mylist[s]
    print('Открываю файл: ', file)
    # Откроем файл
    os.startfile(file)
    
# Функция которая вставляет текст в любое поле любого окна
def pastetxt(txt):
    # Сперва мы копируем содержимое буфера обмена в переменную
    # чтобы не потерять если что-то было скопировано
    buffer = pyperclip.paste()
    # Теперь мы копируем в буфер обмена наш сказанный текст
    pyperclip.copy(txt.capitalize() + '. ')
    # Делаем паузу
    time.sleep(0.7)
    # Эмулируем нажатие клавиш для вставки скопированного
    keyboard.press_and_release('ctrl + v')
    # Снова пауза
    time.sleep(0.5)
    # Возвращаем в буфер обмена то что в нём было ранее
    pyperclip.copy(buffer)

# Функция которая открывает поиск в браузере с соответствующим запросом
def findtxt(txt):
    webbrowser.open('https://google.com/search?q=' + txt.replace(' ', '+'))

# Ожидаем голосовых команд 
while True:
    # Получаем с микрофона порцию звука
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        continue
    # Если что-то распозналось
    if rec.AcceptWaveform(data):
        # Получаем распознанный текст
        txt = json.loads(rec.Result())["text"]
        # Если он не пустой
        if txt.strip() != '':
            # Печатаем его на экране
            print('Вы сказали: ', txt)
            
            # Ищем ключевые слова
            flagword = isflag(txt, flags)
            # Если они найдены
            if flagword != None:
                # Очищаем сказанный текст от ключевых слов
                txt = txt.replace(flagword, '').strip()
                # и вставляем его в текущее активное поле ввода
                pastetxt(txt)
                
            # Ищем ключевые слова
            flagword2 = isflag(txt, flags2)
            # Если они найдены
            if flagword2 != None:
                # Очищаем сказанный текст от ключевых слов
                txt = txt.replace(flagword2, '').strip()
                # ищем сказанный текст в гугле
                findtxt(txt)
                
            # Ищем ключевые слова
            flagword3 = isflag(txt, flags3)
            # Если они найдены
            if flagword3 != None:
                # Очищаем сказанный текст от ключевых слов
                txt = txt.replace(flagword3, '').strip()
                # ищем сказанный текст в гугле
                openfile(txt)

