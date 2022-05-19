# Подключим модуль os
# отвечающий за взаимодействие с файловой системой os
import os
import platform

# Напечатает нам аббревиатуру нашей операционной системы
# К примеру -  posix, nt, os2, ce, java, riscos 
print(os.name)
print('______________\n')

# Напечатает переменные среды окружения
print(os.environ)
print('______________\n')

# Получаем значение конкретной переменной окружения
print(os.getenv("COMPUTERNAME"))
print('______________\n')

print(platform.platform())
print(platform.processor())
print('______________\n')
