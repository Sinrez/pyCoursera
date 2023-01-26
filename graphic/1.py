#!/usr/bin/python
from PIL import Image
import os, sys
path = "img2" # Путь до папки с картинками
dirs = os.listdir(path)
def resize():
    for item in dirs:
        if os.path.isfile(path+'/'+item):
            im = Image.open(path+'/'+item)
            f, e = os.path.splitext(path+'/'+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


if __name__ =='__main__':
    resize()
