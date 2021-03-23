import sys
import os

# print(sys.platform)
if sys.platform == "linux" or sys.platform == "linux2":
    print('linux')
elif sys.platform == "darwin":
    print('MAC')
elif sys.platform == "win32":
    print('Windows...')

print(os.getcwd())
print("Operating System:", os.name)
print("Information of current operating system: ",os. uname())
print("Current Working Directory: ", os.getcwd())