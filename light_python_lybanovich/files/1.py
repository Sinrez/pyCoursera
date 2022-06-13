import os

print(os.path.exists('/light_python_lybanovich/today.txt'))

print(os.lstat('.'))

print(os.listdir('.'))

print(os.listdir('..'))

test = 'This.is.a.test.of.the.emergency.text.system'

with open('test.txt', 'wt') as ts:
    ts.write(test)