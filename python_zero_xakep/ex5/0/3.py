# Существует несколько способов связаться с созданным вами процессом.
# Например, метод communicate

import subprocess

# Получим список запущенных служб 
# args = ["sc", "query"]

args = ["ls", "-l"] # Для Linux

process = subprocess.Popen(args, stdout=subprocess.PIPE)
 
data = process.communicate()
for line in data:
    if line:
        print(line.decode('cp866'))
