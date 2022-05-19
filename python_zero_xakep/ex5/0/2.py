# Класс Popen Python выполняет дочернюю программу в новом процессе.
# В отличие от метода call, он не дожидается конца выполнения вызванного процесса,
# если вы не укажете это в методе wait.

import subprocess
 
# program = "notepad.exe"
program = "Terminal" # Для Linux
process = subprocess.Popen(program)
#code = process.wait()
#print(code)
print("Программа завершена, а процесс еще работает!")
