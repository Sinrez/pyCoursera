import os.path
from datetime import datetime # для преобразования даты в приемлемый формат

path = r'C:\Windows\notepad.exe'
size = os.path.getsize(path) # размер файла в байтах
ksize = size // 1024 # размер в килобайтах ( // это целочисленное деление)
atime = os.path.getatime(path) # дата последнего доступа в секундах с начала эпохи
mtime = os.path.getmtime(path) # дата последней модификации в секундах с начала эпохи
print ('Размер: ', ksize, ' KB')
print ('Дата последнего использования: ', datetime.fromtimestamp(atime))
print ('Дата последнего редактирования: ', datetime.fromtimestamp(mtime))
