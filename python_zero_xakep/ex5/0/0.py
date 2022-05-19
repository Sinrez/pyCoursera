import subprocess

# Функция call - позволяет вам вызывать другую программу,
# и дождаться её завершения.
 
# Для Windows
# x = subprocess.call("Терминал.app")
 
# Для linux
x = subprocess.call("Terminal.app")

if x == 0:
    print("Success!")
else:
    print("Error!")

