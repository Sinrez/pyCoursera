# pip install pygame
import pygame
import os
import threading
# pip install fuzzywuzzy
from fuzzywuzzy import fuzz

# Инициализируем миксер для проигрывания музыки
pygame.mixer.init()

musicpath='Music/'

# Отдельная функция-заготовка для вынесения 
# последующих функций в отдельный поток
def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        # Делаем поток демоном - благодаря этому он выключается при выходе из программы
        my_thread.daemon = True
        my_thread.start()
    return wrapper

# Выше мы описали функцию-заготовку для создания потока и назвали ее thread.
# Теперь, если мы будем писать перед любой функцией строчку @thread
# то эта функция станет выполняться в отдельном потоке.
# Это очень удобно. Всего лишь @thread над именем функции
# и вот она уже исполняется в новом потоке.


# Функция которая ищет в папке Music mp3 файл по похожему имени
def getmp3(mp3path, text):
    songname = ''
    oldn = 0
    for root, dirs, files in os.walk(mp3path):
        for name in files:
            fullname = os.path.join(root, name)
            if os.path.isfile(fullname) and '.mp3' in fullname:
                name = name.replace('.mp3', '')
                # Если строка присутствует в имени файла, то выходим из цикла
                if text in name.lower():
                    songname = fullname
                    return songname
                n=fuzz.ratio(text, name.lower())
                # Если она более похожа чем предыдущая
                if n > oldn:
                    # В target записываем ответ
                    songname = fullname
                    # Обновляем переменную в которой хранится предыдущая фраза
                    oldn = n               
    return songname

# Функция запускающая проигрывание музыки
@thread
def playmp3(mp3path):
    if os.path.exists(mp3path):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(mp3path)
        pygame.mixer.music.play()
    else:
        print('Песня не найдена')

# Бесконечный цикл ожидающий ввода названия песни или его части
s=''
while s.lower() != 'выход':
    s = input('Введите название песни: ')
    if s.lower() == 'выход':
        pygame.mixer.music.stop()
        break
    else:
        song = getmp3(musicpath, s.lower())
        print(song)
        playmp3(song)
    

# Эта программа была создана как пример работы с потоками
# Но есть один маленький нюанс, касаемый PyGame )
